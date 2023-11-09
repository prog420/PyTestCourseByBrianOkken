`pytest --setup-show -v ch_3_pytest_fixtures/scopes`

```text
ch_3_pytest_fixtures/scopes/package_scope_one/test_scope_one.py::test_scope_class_one 
SETUP    S _session_faker     
      SETUP    C CLASS_FIXTURE
        ch_3_pytest_fixtures/scopes/package_scope_one/test_scope_one.py::test_scope_class_one PASSED    
      TEARDOWN C CLASS_FIXTURE

ch_3_pytest_fixtures/scopes/package_scope_one/test_scope_one.py::test_scope_module_one 
    SETUP    M MODULE_FIXTURE
        ch_3_pytest_fixtures/scopes/package_scope_one/test_scope_one.py::test_scope_module_one PASSED  

ch_3_pytest_fixtures/scopes/package_scope_one/test_scope_one.py::test_scope_package_one 
  SETUP    P PACKAGE_FIXTURE
        ch_3_pytest_fixtures/scopes/package_scope_one/test_scope_one.py::test_scope_package_one PASSED

ch_3_pytest_fixtures/scopes/package_scope_one/test_scope_one.py::TestScopeOne::test_class_scope_one 
      SETUP    C CLASS_FIXTURE
        ch_3_pytest_fixtures/scopes/package_scope_one/test_scope_one.py::TestScopeOne::test_class_scope_one PASSED
      TEARDOWN C CLASS_FIXTURE
    TEARDOWN M MODULE_FIXTURE

ch_3_pytest_fixtures/scopes/package_scope_two/test_scope_two.py::test_scope_class_two
      SETUP    C CLASS_FIXTURE
        ch_3_pytest_fixtures/scopes/package_scope_two/test_scope_two.py::test_scope_class_two PASSED
      TEARDOWN C CLASS_FIXTURE

ch_3_pytest_fixtures/scopes/package_scope_two/test_scope_two.py::test_scope_module_two
    SETUP    M MODULE_FIXTURE
        ch_3_pytest_fixtures/scopes/package_scope_two/test_scope_two.py::test_scope_module_two PASSED

ch_3_pytest_fixtures/scopes/package_scope_two/test_scope_two.py::test_scope_package_two
        ch_3_pytest_fixtures/scopes/package_scope_two/test_scope_two.py::test_scope_package_two PASSED

ch_3_pytest_fixtures/scopes/package_scope_two/test_scope_two.py::TestScopeTwo::test_class_scope_two
      SETUP    C CLASS_FIXTURE
        ch_3_pytest_fixtures/scopes/package_scope_two/test_scope_two.py::TestScopeTwo::test_class_scope_two PASSED
      TEARDOWN C CLASS_FIXTURE
    TEARDOWN M MODULE_FIXTURE

TEARDOWN S _session_faker
  TEARDOWN P PACKAGE_FIXTURE
```