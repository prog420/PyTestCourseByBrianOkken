### <span style="color: #46ab64;"> Chapter 7. Test Strategy
___
AUT: [Cards (To-Do List)](https://pypi.org/project/cards/)

1. Test the behaviours and features that are accessible through the end user interface, the CLI.
2. Test those features through the API as much as possible.
3. Test the CLI enough to verify the API is getting properly called for all features.
4. Test the following core features thoroughly: `add`, `count`, `delete`, `finish`, `list`, `start`, `update`.
5. Include tests for `config` and `version`.
6. Test TinyDB subsystem integration with `db.py`.


#### <span style="color: #46ab64;"> Prioritizing:

1. Recent - New features / areas of code, new functionality that has been recentrly repaired / refactored / modified.
2. Core - The essential functions that must continue to work in order for the product to be useful.
3. Risk - Areas important to customers, but not used regularly by the dev team or parts that use 3rd-party code you don't quite trust.
4. Problematic - Functionality that frequently breaks or often gets defect reports against it.
5. Expertise - Features or algorithms understood by a limited subset of people.

#### <span style="color: #46ab64;"> Creating Test Cases:

* Start with a non-trivial, happy path test case.
* Then look at test cases that represent:
  * interesting sets of input
  * interesting starting states
  * interesting end states, or
  * possible error states.