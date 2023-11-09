### <span style="color: #46ab64;"> Chapter 1. Getting Started.
___
#### <span style="color: #46ab64;"> 0. Installation

1. New Environment:

`python -m venv venv`

2. Activate new Environment:

`source venv/bin/activate` (Linux) or `venv\Scripts\activate.bat` (Windows)

3. Install PyTest

`pip install pytest`


#### <span style="color: #46ab64;"> 1. Naming Conventions

1. Test Files: `test_<something>.py` or `<something>_test.py`
2. Test Methods / Functions: `test_something`
3. Test Classes: `Test<Something>`


#### <span style="color: #46ab64;"> 2. Possible Outcomes of a test

1. PASSED (.) - The test ran successfully.
2. FAILED (F) - The test did not run successfully.
3. SKIPPED (s) - The test was skipped (`@pytest.mark.skip`)
4. XFAIL (x) - The test was not supposed to pass, and it ran and failed (`@pytest.mark.xfail`).
5. XPASS (X) - The test was marked with `xfail`, but it ran and passed.
6. ERROR (E) - An exception happened either during the execution of a fixture or hook function and not during the execution of a test function.

#### <span style="color: #46ab64;"> 3. PyTest CLI Arguments

`_pytest/terminal.py`:

   * `-v` or `--verbose`: increase verbosity.
   * `-q` or `--quiet`: decrease verbosity.
   * `--no-header`: disable header.
   * `--no-summary`: disable summary ('short test summary info').
   * `-tb` (`auto`, `long`, `short`, `no`, `line`, `native`): traceback options.
   * `--verbosity {int}`: set verbosity to `{int}`. Default: `0`.
   * `--show-capture` (`no`, `stdout`, `stderr`, `log`, `all`): controls how captured stdout/stderr/log is shown on failed tests. Default: `all`.
   * `--fulltrace`: don't cut any tracebacks (default is to cut).

`_pytest/python.py`:

   * `--fixtures`: show available fixtures, sorted by plugin appearance (fixtures with leading `_` are only shown with `-v`)
   * `--fixtures-per-test`: show used fixtures per test

`_pytest/main.py`:

   * `--collectonly` or `--collect-only` or `--co`: only collect tests, don't execute them.
   * `-x` or `--exitfirst`: exit instantly on first error or failed test.
   * `--maxfail {num}`: exit after first `{num}` failures or errors.
   * `--strict-config`: any warnings encountered while parsing the `pytest` section of the configuration file raise errors.
   * `--strict-markers`: markers not registered in the `markers` section of the configuration file raise errors.
   * `-c {file}` or `--config-file {file}`: Load configuration from `{file}` instead of trying to locate one of the implicit configuration files.
   * `--rootdir`: define root directory for tests. Can be relative path: 'root_dir', './root_dir', 'root_dir/another_dir/'; absolute path: '/home/user/root_dir'; path with variables: '$HOME/root_dir'.
   * `--keepduplicates`: keep duplicate tests.
   * `--basetemp`: base temporary directory for this test run.