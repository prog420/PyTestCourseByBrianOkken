### <span style="color: #46ab64;"> Chapter 2. Writing Test Functions.
___
AUT: [Cards (To-Do List)](https://pypi.org/project/cards/)

#### <span style="color: #46ab64;"> 1. Assertion Helper Functions

1. `pytest.fail(reason: str)` can be used to write custom checks.
2. `__tracebackhide__ == True`: assertion helper function won't be included to the traceback output.
3. `pytest.raises(expected_exception: Exception)`: expected exception.


#### <span style="color: #46ab64;"> 2. Structuring Test Functions

Common pattern: separate test into stages.

* **Arrange - Act - Assert** (Bill Wake, 2001, Kent Beck later popularized the practice as part of TDD)

* **Given - When - Then** (Ivan Moore, BDD)

1. **Arrange / Given** - A starting state. Set up data / env to get ready for the action.
2. **Act / When** - Some action is performed.
3. **Assert / Then** - Some expected result or end state should happen. At the end of the test, we make sure the action resulted in the expected behavior.


#### <span style="color: #46ab64;"> 3. Running Subset of Tests

| Subset                        | Syntax                                               |
|-------------------------------|------------------------------------------------------|
| Single test method            | `pytest path/test_module.py::TestClass::test_method` |
| All tests in a class          | `pytest path/test_module.py::TestClass`              |
| Single test function          | `pytest path/test_moudle.py::test_function`          |
| All tests in a module         | `pytest path/test_module.py`                         |
| All tests in a directory      | `pytest path`                                        |
| Tests matching a name pattern | `pytest -k pattern`                                  |
| Tests by marker               | `pytest -m <mark>` (Chapter 6)                       |