### Notes from [_Python Testing with pytest_ by Brian Okken](https://pythontest.com/pytest-book/).

#### Contents:

* [**ch_2**](/ch_2_writing_test_functions) - Writing Test Functions
  * Structuring Test Functions
  * Grouping Tests with Classes
  * Running a Subset of Tests
* [**ch_3**](/ch_3_pytest_fixtures) - pytest Fixtures
  * Setup / Teardown
  * Tracing Fixture execution
  * Fixture Scope
  * Sharing Fixtures through `conftest.py`
  * `autouse`
* [**ch_4**](/ch_4_builtin_fixtures) - Builtin Fixtures
  * `tmp_path` and `tmp_path_factory`
  * `capsys`
  * `monkeypatch`
* [**ch_5**](/ch_5_parametrization) - Parametrization
  * Parametrizing Functions
  * Parametrizing Fixtures
  * Parametrizing with `pytest_generate_tests`
* [**ch_6**](/ch_6_markers) - Markers
  * Builting Markers
  * Skipping Tests with `pytest.mark.skip`
  * Skipping Tests conditionally with `pytest.mark.skipif`
  * Expecting Tests to Fail with `pytest.mark.fail`
  * Selecting Tests with Custom Markers
  * Marking Files, Classes and Parameters
* [**ch_7**](/ch_7_test_plan) - Strategy
* [**ch_8**](/ch_8_config_files) - Configuration Files
  * `pytest.ini`
  * `tox.ini`
  * `pyproject.toml`
  * `setup.cfg`
  * Root Directory and config file
* [**ch_9**](/ch_9_coverage) - Coverage
  * `pytest-cov`
* [**ch_10**](/ch_10_mocks) - Mocking
  * Mocking an Attribute
  * Mocking a Class and Methods
  * Keeping Mock and Implementation in Sync with Autospec
