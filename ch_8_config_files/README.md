### <span style="color: #46ab64;"> Chapter 8. Config Files.
___
AUT: [Cards (To-Do List)](https://pypi.org/project/cards/)


#### <span style="color: #46ab64;"> 1. Non-test files relevant to pytest

1. `pytest.ini` - primary pytest configuration file that allows you to change pytest's default behaviour.
2. `conftest.py` - that file contains fixtures and hook functions. It can exist at the `rootdir` or in any subdirectory.
3. `__init__.py` - when put into test subdirectories, this file allows you to have identical test file names in multiple test directories.
4. `tox.ini`, `pyproject.toml`, `setup.cfg` - these files can take the place of `pytest.ini`.
   * `tox.ini` is used by tox, the CLI automated testing tool;
   * `pyproject.toml` is used for packaging Python projects and can be used to save settings for various tool, including pytest.
   * `setup.cfg` is also used for packaging and can be used to save pytest settings.

#### <span style="color: #46ab64;"> 1. `pytest.ini`

1. The `addopts` setting enables us to list the pytest flags we always want
to run in this project.
2. `--strict-markers` tells pytest to raise an error for any unregistered marker
encountered in the test code as opposed to a warning. Turn this on
to avoid marker-name typos.
3. `--strict-config` tells pytest to raise an error for any difficulty in parsing
configuration files. The default is a warning. Turn this on to avoid
configuration-file typos going unnoticed.
4. `-ra` tells pytest to display extra test summary information at the end
of a test run. The default is to show extra information on only test
failures and errors. The `a` part of `-ra` tells pytest to show information
on everything except passing tests. This adds skipped, xfailed, and
xpassed to the failure and error tests