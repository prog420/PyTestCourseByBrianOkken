### <span style="color: #46ab64;"> Chapter 6. Markers
___
AUT: [Cards (To-Do List)](https://pypi.org/project/cards/)

#### <span style="color: #46ab64;"> 1. Builtin Markers

* `@pytest.mark.filterwarnings(warning)`
* `@pytest.mark.skip(reason=None)` - skip the test with an optional reason.
* `@pytest.mark.skipif(condition, ..., *, reason)` - skip if any of the conditions are True.
* `@pytest.mark.xfail(condition, ..., *, reason, run=True, raises=None, strict=xfail_strict)` - we expect this test to fail.
* `@pytest.mark.paramterize(argnames, argvalues, indirect, ids, scope)` - call  test with different arguments.
* `@pytest.mark.usefixtures(fixturename1, fixturename2, ...)` - mark test as needing all the specified fixtures.


#### <span style="color: #46ab64;"> 2. Special Markers

**1. File-level Markers.**

```python
import pytest

pytestmark = pytest.mark.skip
...
```

It will apply the marker to all the tests in that module.

_Multiple markers:_

`pytestmark = [pytest.mark.marker_one, pytest.mark.marker_two]`


**2. Parametrized Test Markers**

```python
import pytest

@pytest.mark.parametrize(
    "state",
    [
        "todo",
        pytest.param("in progress", marks=pytest.mark.smoke),
        "done"
    ]
)
def test_state(state):
    ...
```


#### <span style="color: #46ab64;"> 3. Subset Selections

1. Simple example:

`pytest -v -m smoke`

2. Markers + `and`, `or`, `not` and Parentheses

`pytest -v -m "smoke and regression"`

`pytest -v -m "smoke and not regression"`

`pytest -v -m "(smoke or regression) and (not api)"`

`pytest -v -m smoke -k "not <TestClass>"`


#### <span style="color: #46ab64;"> 4. `--strict-markers`


1. **Without `--strict-markers`:**

Typo in marker (e.g. `@pytest.mark.smok` instead of `@pytest.mark.smoke`) => **Warning at runtime**:

```text
=========================== warnings summary ===========================
test_start.py:17
/path/to/code/ch6/bad/test_start.py:17:
PytestUnknownMarkWarning:
Unknown pytest.mark.smok - is this a typo? ...
@pytest.mark.smok
...
============== 7 passed, 5 deselected, 1 warning in 0.06s ==============
```

2. **With `--strict-markers`:**

Typo in marker => **Error at the test collection step:**

```text
================================ ERRORS ================================
____________________ ERROR collecting test_start.py ____________________
'smok' not found in `markers` configuration option
======================= short test summary info ========================
ERROR test_start.py
!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!
==================== 4 deselected, 1 error in 0.15s ====================
```

#### <span style="color: #46ab64;"> 5. `pytest.ini` (with --strict-markers)

`pytest.ini` can be used to store markers or options:

Example:

```text
[pytest]
markers = 
    smoke: subset of tests
    regression: full regression set
addopts =
    --strict-markers
```


#### <span style="color: #46ab64;"> 6. Combining Markers with Fixtures

1. Setup processing for your custom marker:

```python
import pytest

@pytest.fixture(scope="function")
def db(request: pytest.FixtureRequest):
    # request.node = pytest's reprentation of a test.
    m = request.node.get_closest_marker("custom_marker")
    if m and len(m.args) > 0:
        marker_arg = m.args[0]
        
        # Do some action based on received information
        ...
```

2. Use custom marker in your test:

```python
import pytest

@pytest.mark.custom_marker(5)
def test_with_custom_marker():
    assert 1 == 1
```


#### <span style="color: #46ab64;"> 7. Listing Markers


`pytest --markers`