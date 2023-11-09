

def test_scope_class_one(class_fixture):
    print(class_fixture)
    assert 1 == 1


def test_scope_module_one(module_fixture):
    print(module_fixture)
    assert 1 == 1


def test_scope_package_one(package_fixture):
    print(package_fixture)
    assert 1 == 1


class TestScopeOne:
    def test_class_scope_one(self, class_fixture):
        print(class_fixture)
        assert 1 == 1
