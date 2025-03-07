# CHANGELOG - IBM WAS

## 1.12.0 / 2021-12-20

* [Security] Bump lxml package. See [#10904](https://github.com/DataDog/integrations-core/pull/10904).

## 1.11.1 / 2021-11-16

* [Fixed] Add dd_run_check and remove unused config options. See [#10623](https://github.com/DataDog/integrations-core/pull/10623).

## 1.11.0 / 2021-11-13

* [Added] Add runtime configuration validation. See [#8936](https://github.com/DataDog/integrations-core/pull/8936).
* [Added] Update dependencies. See [#10580](https://github.com/DataDog/integrations-core/pull/10580).

## 1.10.1 / 2021-10-12 / Agent 7.32.0

* [Fixed] Bump base package requirements. See [#10390](https://github.com/DataDog/integrations-core/pull/10390).

## 1.10.0 / 2021-10-04

* [Added] Sync configs with new option and bump base requirement. See [#10315](https://github.com/DataDog/integrations-core/pull/10315).
* [Added] Change status warning to debug log. See [#10278](https://github.com/DataDog/integrations-core/pull/10278).
* [Added] Add HTTP option to control the size of streaming responses. See [#10183](https://github.com/DataDog/integrations-core/pull/10183).
* [Added] Add allow_redirect option. See [#10160](https://github.com/DataDog/integrations-core/pull/10160).
* [Fixed] Fix the description of the `allow_redirects` HTTP option. See [#10195](https://github.com/DataDog/integrations-core/pull/10195).
* [Fixed] Add server as generic tag. See [#10100](https://github.com/DataDog/integrations-core/pull/10100).

## 1.9.0 / 2021-04-19 / Agent 7.28.0

* [Security] Upgrade lxml python package. See [#9173](https://github.com/DataDog/integrations-core/pull/9173).

## 1.8.2 / 2021-03-07 / Agent 7.27.0

* [Fixed] Bump minimum base package version. See [#8443](https://github.com/DataDog/integrations-core/pull/8443).

## 1.8.1 / 2020-12-23 / Agent 7.25.0

* [Fixed] Bump lxml to 4.6.2. See [#8249](https://github.com/DataDog/integrations-core/pull/8249).

## 1.8.0 / 2020-12-11

* [Added] Refactor to only parse configuration once. See [#8025](https://github.com/DataDog/integrations-core/pull/8025).
* [Added] Add config specs. See [#8024](https://github.com/DataDog/integrations-core/pull/8024).

## 1.7.0 / 2020-06-29 / Agent 7.21.0

* [Added] Add note about warning concurrency. See [#6967](https://github.com/DataDog/integrations-core/pull/6967).

## 1.6.0 / 2020-05-17 / Agent 7.20.0

* [Added] Upgrade lxml to 4.5.0. See [#6661](https://github.com/DataDog/integrations-core/pull/6661).
* [Added] Allow optional dependency installation for all checks. See [#6589](https://github.com/DataDog/integrations-core/pull/6589).

## 1.5.1 / 2020-04-04 / Agent 7.19.0

* [Fixed] Remove logs sourcecategory. See [#6121](https://github.com/DataDog/integrations-core/pull/6121).

## 1.5.0 / 2020-01-13 / Agent 7.17.0

* [Added] Use lazy logging format. See [#5377](https://github.com/DataDog/integrations-core/pull/5377).

## 1.4.0 / 2019-12-02 / Agent 7.16.0

* [Added] Add auth type to RequestsWrapper. See [#4708](https://github.com/DataDog/integrations-core/pull/4708).

## 1.3.1 / 2019-10-17 / Agent 6.15.0

* [Fixed] Fix character casing logic for custom_queries_units_gauge option. See [#4796](https://github.com/DataDog/integrations-core/pull/4796).

## 1.3.0 / 2019-10-11

* [Added] Add an option for custom count with units. See [#4628](https://github.com/DataDog/integrations-core/pull/4628).

## 1.2.3 / 2019-09-23

* [Fixed] Don't assume nested tags exist. See [#4605](https://github.com/DataDog/integrations-core/pull/4605).

## 1.2.2 / 2019-09-02 / Agent 6.14.0

* [Fixed] Fix bug where multinode clusters would report wrong server/node tag combination and duplicate metric values. See [#4491](https://github.com/DataDog/integrations-core/pull/4491).

## 1.2.1 / 2019-08-30

* [Fixed] Update class signature to support the RequestsWrapper. See [#4469](https://github.com/DataDog/integrations-core/pull/4469).

## 1.2.0 / 2019-08-02

* [Added] Update metric type for JVM Metrics. See [#4085](https://github.com/DataDog/integrations-core/pull/4085).

## 1.1.0 / 2019-05-14 / Agent 6.12.0

* [Added] Use request wrapper. See [#3650](https://github.com/DataDog/integrations-core/pull/3650).
* [Added] Adhere to code style. See [#3520](https://github.com/DataDog/integrations-core/pull/3520).

## 1.0.0 / 2019-02-20 / Agent 6.10.0

* [Added] Create IBM WAS Integration. See [#2846](https://github.com/DataDog/integrations-core/pull/2846).

