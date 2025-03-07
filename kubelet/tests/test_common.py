# (C) Datadog, Inc. 2018-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
import json
import os
import sys

import mock
import pytest

from datadog_checks.base.checks.kubelet_base.base import KubeletCredentials, urljoin
from datadog_checks.base.checks.openmetrics import OpenMetricsBaseCheck
from datadog_checks.kubelet import PodListUtils, get_pod_by_uid, is_static_pending_pod

from .test_kubelet import mock_from_file

# Skip the whole tests module on Windows
pytestmark = pytest.mark.skipif(sys.platform == 'win32', reason='tests for linux only')

# Constants
HERE = os.path.abspath(os.path.dirname(__file__))


def test_container_filter(monkeypatch):
    c_is_excluded = mock.Mock(return_value=False)
    monkeypatch.setattr('datadog_checks.kubelet.common.c_is_excluded', c_is_excluded)

    long_cid = "docker://a335589109ce5506aa69ba7481fc3e6c943abd23c5277016c92dac15d0f40479"
    ctr_name = "datadog-agent"
    ctr_image = "datadog/agent-dev:haissam-tagger-pod-entity"
    namespace = "default"

    pods = json.loads(mock_from_file('pods.json'))
    pod_list_utils = PodListUtils(pods)

    assert pod_list_utils is not None
    assert len(pod_list_utils.containers) == 10
    assert long_cid in pod_list_utils.containers
    c_is_excluded.assert_not_called()

    # Test cid == None
    c_is_excluded.reset_mock()
    assert pod_list_utils.is_excluded(None) is True
    c_is_excluded.assert_not_called()

    # Test cid == ""
    c_is_excluded.reset_mock()
    assert pod_list_utils.is_excluded("") is True
    c_is_excluded.assert_not_called()

    # Test non-existing container
    c_is_excluded.reset_mock()
    assert pod_list_utils.is_excluded("invalid") is True
    c_is_excluded.assert_not_called()

    # Test existing unfiltered container
    c_is_excluded.reset_mock()
    assert pod_list_utils.is_excluded(long_cid) is False
    c_is_excluded.assert_called_once()
    c_is_excluded.assert_called_with(ctr_name, ctr_image, namespace)

    # Clear exclusion cache
    pod_list_utils.cache = {}

    # Test existing filtered container
    c_is_excluded.reset_mock()
    c_is_excluded.return_value = True
    assert pod_list_utils.is_excluded(long_cid) is True
    c_is_excluded.assert_called_once()
    c_is_excluded.assert_called_with(ctr_name, ctr_image, namespace)


def test_filter_staticpods(monkeypatch):
    c_is_excluded = mock.Mock(return_value=True)
    monkeypatch.setattr('datadog_checks.kubelet.common.c_is_excluded', c_is_excluded)

    pods = json.loads(mock_from_file('pods.json'))
    pod_list_utils = PodListUtils(pods)

    # kube-proxy-gke-haissam-default-pool-be5066f1-wnvn is static
    assert pod_list_utils.is_excluded("cid", "260c2b1d43b094af6d6b4ccba082c2db") is False
    c_is_excluded.assert_not_called()

    # fluentd-gcp-v2.0.10-9q9t4 is not static
    assert (
        pod_list_utils.is_excluded(
            "docker://5741ed2471c0e458b6b95db40ba05d1a5ee168256638a0264f08703e48d76561",
            "2edfd4d9-10ce-11e8-bd5a-42010af00137",
        )
        is True
    )


def test_is_namespace_excluded(monkeypatch):
    c_is_excluded = mock.Mock(return_value=False)
    monkeypatch.setattr('datadog_checks.kubelet.common.c_is_excluded', c_is_excluded)

    pods = json.loads(mock_from_file('pods.json'))
    pod_list_utils = PodListUtils(pods)

    # Test namespace=None
    c_is_excluded.reset_mock()
    assert pod_list_utils.is_namespace_excluded(None) is False
    c_is_excluded.assert_not_called()

    # Test excluded namespace
    c_is_excluded.reset_mock()
    c_is_excluded.return_value = True
    assert pod_list_utils.is_namespace_excluded('an_excluded_namespace') is True
    c_is_excluded.assert_called_once()
    c_is_excluded.assert_called_with('', '', 'an_excluded_namespace')

    # Test non-excluded namespace
    c_is_excluded.reset_mock()
    c_is_excluded.return_value = False
    assert pod_list_utils.is_namespace_excluded('a_non_excluded_namespace') is False
    c_is_excluded.assert_called_once()
    c_is_excluded.assert_called_with('', '', 'a_non_excluded_namespace')


def test_pod_by_uid():
    podlist = json.loads(mock_from_file('pods.json'))

    pod = get_pod_by_uid("260c2b1d43b094af6d6b4ccba082c2db", podlist)
    assert pod is not None
    assert pod["metadata"]["name"] == "kube-proxy-gke-haissam-default-pool-be5066f1-wnvn"

    pod = get_pod_by_uid("unknown", podlist)
    assert pod is None


def test_url_join():
    res = urljoin("https://10.100.0.1:443/api/fargate-XX.us-east-2.compute.internal/proxy", "/pods")
    assert res == 'https://10.100.0.1:443/api/fargate-XX.us-east-2.compute.internal/proxy/pods'
    res = urljoin("https://10.100.0.1:443/api/fargate-XX.us-east-2.compute.internal/proxy", "pods")
    assert res == 'https://10.100.0.1:443/api/fargate-XX.us-east-2.compute.internal/proxy/pods'
    res = urljoin("https://10.100.0.1:443/api/fargate-XX.us-east-2.compute.internal/proxy/", "pods")
    assert res == 'https://10.100.0.1:443/api/fargate-XX.us-east-2.compute.internal/proxy/pods'
    res = urljoin("https://10.100.0.1:443/api/fargate-XX.us-east-2.compute.internal/proxy/", "/pods")
    assert res == 'https://10.100.0.1:443/api/fargate-XX.us-east-2.compute.internal/proxy/pods'


def test_is_static_pod():
    podlist = json.loads(mock_from_file('pods.json'))

    # kube-proxy-gke-haissam-default-pool-be5066f1-wnvn is static
    pod = get_pod_by_uid("260c2b1d43b094af6d6b4ccba082c2db", podlist)
    assert pod is not None
    assert is_static_pending_pod(pod) is True

    # fluentd-gcp-v2.0.10-9q9t4 is not static
    pod = get_pod_by_uid("2edfd4d9-10ce-11e8-bd5a-42010af00137", podlist)
    assert pod is not None
    assert is_static_pending_pod(pod) is False


def test_credentials_empty():
    creds = KubeletCredentials({})
    assert creds.verify() is None
    assert creds.cert_pair() is None
    assert creds.headers("https://dummy") is None

    instance = {'prometheus_url': 'https://dummy', 'namespace': 'foo'}
    scraper = OpenMetricsBaseCheck('prometheus', {}, [instance])
    scraper_config = scraper.create_scraper_configuration(instance)
    creds.configure_scraper(scraper_config)
    assert scraper_config['ssl_ca_cert'] is None
    assert scraper_config['ssl_cert'] is None
    assert scraper_config['ssl_private_key'] is None
    assert scraper_config['extra_headers'] == {}


def test_credentials_certificates():
    creds = KubeletCredentials(
        {"verify_tls": "true", "ca_cert": "ca_cert", "client_crt": "crt", "client_key": "key", "token": "ignore_me"}
    )
    assert creds.verify() == "ca_cert"
    assert creds.cert_pair() == ("crt", "key")
    assert creds.headers("https://dummy") is None

    instance = {'prometheus_url': 'https://dummy', 'namespace': 'foo'}
    scraper = OpenMetricsBaseCheck('prometheus', {}, [instance])
    scraper_config = scraper.create_scraper_configuration(instance)
    creds.configure_scraper(scraper_config)
    assert scraper_config['ssl_ca_cert'] == "ca_cert"
    assert scraper_config['ssl_cert'] == "crt"
    assert scraper_config['ssl_private_key'] == "key"
    assert scraper_config['extra_headers'] == {}


def test_credentials_token_noverify():
    expected_headers = {'Authorization': 'Bearer mytoken'}
    creds = KubeletCredentials(
        {"verify_tls": "false", "ca_cert": "ca_cert", "client_crt": "ignore_me", "token": "mytoken"}
    )
    assert creds.verify() is False
    assert creds.cert_pair() is None
    assert creds.headers("https://dummy") == expected_headers
    # Make sure we don't leak the token over http
    assert creds.headers("http://dummy") is None

    instance = {'prometheus_url': 'https://dummy', 'namespace': 'foo'}
    scraper = OpenMetricsBaseCheck('prometheus', {}, [instance])
    scraper_config = scraper.create_scraper_configuration(instance)
    creds.configure_scraper(scraper_config)
    assert scraper_config['ssl_ca_cert'] is False
    assert scraper_config['ssl_cert'] is None
    assert scraper_config['ssl_private_key'] is None
    assert scraper_config['extra_headers'] == expected_headers

    # Make sure we don't leak the token over http
    scraper_config['prometheus_url'] = "http://dummy"
    creds.configure_scraper(scraper_config)
    assert scraper_config['ssl_ca_cert'] is False
    assert scraper_config['ssl_cert'] is None
    assert scraper_config['ssl_private_key'] is None
    assert scraper_config['extra_headers'] == {}
