# CHANGELOG - SAP HANA

## 1.10.0 / 2021-11-24

* [Added] Add support for only_custom_queries. See [#10695](https://github.com/DataDog/integrations-core/pull/10695).

## 1.9.0 / 2021-11-13

* [Added] Support the `hdbcli` client library. See [#10595](https://github.com/DataDog/integrations-core/pull/10595).
* [Fixed] Resolve unexpected errors when statuses other than 'running' or 'idle' are received. See [#10333](https://github.com/DataDog/integrations-core/pull/10333).

## 1.8.2 / 2021-10-15 / Agent 7.32.0

* [Fixed] Ensure `persist_db_connections` is read from init_config. See [#10417](https://github.com/DataDog/integrations-core/pull/10417).
* [Fixed] Bump base package requirements. See [#10390](https://github.com/DataDog/integrations-core/pull/10390).

## 1.8.1 / 2021-10-12

* [Fixed] Bump base package requirements. See [#10390](https://github.com/DataDog/integrations-core/pull/10390).

## 1.8.0 / 2021-10-04

* [Added] Sync configs with new option and bump base requirement. See [#10315](https://github.com/DataDog/integrations-core/pull/10315).

## 1.7.0 / 2021-09-20

* [Added] Add option to disable persistent database connections. See [#10023](https://github.com/DataDog/integrations-core/pull/10023).
* [Added] Disable generic tags. See [#10027](https://github.com/DataDog/integrations-core/pull/10027).
* [Fixed] Add server as generic tag. See [#10100](https://github.com/DataDog/integrations-core/pull/10100).

## 1.6.0 / 2021-08-22 / Agent 7.31.0

* [Added] Use `display_default` as a fallback for `default` when validating config models. See [#9739](https://github.com/DataDog/integrations-core/pull/9739).

## 1.5.0 / 2021-07-12 / Agent 7.30.0

* [Added] Add runtime configuration validation. See [#8981](https://github.com/DataDog/integrations-core/pull/8981).

## 1.4.1 / 2021-03-07 / Agent 7.27.0

* [Fixed] Catch exception when closing lost connection. See [#8630](https://github.com/DataDog/integrations-core/pull/8630).
* [Fixed] Rename config spec example consumer option `default` to `display_default`. See [#8593](https://github.com/DataDog/integrations-core/pull/8593).
* [Fixed] Bump minimum base package version. See [#8443](https://github.com/DataDog/integrations-core/pull/8443).

## 1.4.0 / 2021-01-25 / Agent 7.26.0

* [Added] Add SSL support for connection. See [#8098](https://github.com/DataDog/integrations-core/pull/8098).

## 1.3.0 / 2020-10-31 / Agent 7.24.0

* [Added] Add config spec. See [#7715](https://github.com/DataDog/integrations-core/pull/7715).

## 1.2.0 / 2020-05-17 / Agent 7.20.0

* [Added] Allow optional dependency installation for all checks. See [#6589](https://github.com/DataDog/integrations-core/pull/6589).

## 1.1.0 / 2020-01-13 / Agent 7.17.0

* [Added] Use lazy logging format. See [#5377](https://github.com/DataDog/integrations-core/pull/5377).

## 1.0.0 / 2019-11-11 / Agent 7.16.1

* [Added] Add SAP HANA integration. See [#4502](https://github.com/DataDog/integrations-core/pull/4502).
