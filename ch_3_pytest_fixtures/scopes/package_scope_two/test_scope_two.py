

def test_scope_class_two(class_fixture):
    print(class_fixture)
    assert 1 == 1


def test_scope_module_two(module_fixture):
    print(module_fixture)
    assert 1 == 1


def test_scope_package_two(package_fixture):
    print(package_fixture)
    assert 1 == 1


class TestScopeTwo:
    def test_class_scope_two(self, class_fixture):
        print(class_fixture)
        assert 1 == 1
