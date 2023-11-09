### <span style="color: #46ab64;"> Chapter 3. PyTest Fixtures
___
AUT: [Cards (To-Do List)](https://pypi.org/project/cards/)


`--setup-show`: trace fixture execution.

#### Example (`test_count.py`):

`$ pytest --setup-show ch_3_pytest_fixtures/test_count.py`

```text
collected 2 items
        SETUP    F cards_db
        ch_3_pytest_fixtures/test_count.py::test_empty (fixtures used: _session_faker, cards_db, request).
        TEARDOWN F cards_db
        SETUP    F cards_db
        ch_3_pytest_fixtures/test_count.py::test_two_cards (fixtures used: _session_faker, cards_db, request).
        TEARDOWN F cards_db
TEARDOWN S _session_faker
```

#### <span style="color: #46ab64;"> 1. Fixture Scopes

1. `function`: Run once per test function (default scope)
2. `class`: Run one per test class
3. `package`: Run once per package or test directory
4. `session`: Run once per session (one setup and one teardown)


#### <span style="color: #46ab64;"> 2. Another Fixture arguments

1. `autouse = True`: get a fixture run every time.
2. `name = <name: str>`: rename fixture.