### <span style="color: #46ab64;"> Chapter 4. Builtin Fixtures
___
AUT: [Cards (To-Do List)](https://pypi.org/project/cards/)

Check all builtin fixtures:

`pytest --fixtures`

#### <span style="color: #46ab64;"> 1. List of Builtin Fixtures

1. `tmp_path`, `tmp_path_factory` - temp directories
2. `capsys` - capturing output
3. `monkeypatch` - changing the env or application code

#### <span style="color: #46ab64;"> 1.1 `tmp_path`, `tmp_path_factory`

Change base directory: `pytest --basetemp=<mydir>`

#### <span style="color: #46ab64;"> 1.2 `capsys`

Related builtin fixtures:

* `caplog` - capture output written with the logging package
* `capdf` - capture file descriptors 1 and 2
* `capsysbinary` - capture bytes
* `capfdbinary` - capture bytes on file descriptors 1 and 2

#### <span style="color: #46ab64;"> 1.3 `monkeypatch`

https://docs.pytest.org/en/7.1.x/how-to/monkeypatch.html

`monkeypatch` functions:

`setattr(target, name, value, raising=True)` - sets an attribute
`delattr(target, name, raising=True)` - deletes an attribute
`setitem(dic, name, value)` - sets a dictionary entry
`delitem(dic, name, raising=True)` - deletes a dictionary entry
`setenv(name, value, prepend=None)` - sets an environment variable
`delenv(name, raising=True)` - deletes an environment variable
`syspath_prepend(path)` - prepend `path` to `sys.path` (Python's list of import locations)
`chdir(path)` - changes the current working directory


Example of `setattr`:

```python
# contents of test_app.py, a simple test for our API retrieval
# import requests for the purposes of monkeypatching
import requests

# our app.py that includes the get_json() function
# this is the previous code block example
import app

# custom class to be the mock return value
# will override the requests.Response returned from requests.get
class MockResponse:

    # mock json() method always returns a specific testing dictionary
    @staticmethod
    def json():
        return {"mock_key": "mock_response"}


def test_get_json(monkeypatch):

    # Any arguments may be passed and mock_get() will always return our
    # mocked object, which only has the .json() method.
    def mock_get(*args, **kwargs):
        return MockResponse()

    # apply the monkeypatch for requests.get to mock_get
    monkeypatch.setattr(requests, "get", mock_get)

    # app.get_json, which contains requests.get, uses the monkeypatch
    result = app.get_json("https://fakeurl")
    assert result["mock_key"] == "mock_response"
```

Fixture:

```python
# contents of test_app.py, a simple test for our API retrieval
import pytest
import requests

# app.py that includes the get_json() function
import app

# custom class to be the mock return value of requests.get()
class MockResponse:
    @staticmethod
    def json():
        return {"mock_key": "mock_response"}


# monkeypatched requests.get moved to a fixture
@pytest.fixture
def mock_response(monkeypatch):
    """Requests.get() mocked to return {'mock_key':'mock_response'}."""

    def mock_get(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr(requests, "get", mock_get)


# notice our test uses the custom fixture instead of monkeypatch directly
def test_get_json(mock_response):
    result = app.get_json("https://fakeurl")
    assert result["mock_key"] == "mock_response"
```