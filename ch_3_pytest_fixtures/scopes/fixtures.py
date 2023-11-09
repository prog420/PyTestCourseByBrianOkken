import pytest


@pytest.fixture(scope="class")
def class_fixture():
    return "class fixture"


@pytest.fixture(scope="module")
def module_fixture():
    return "module fixture"


@pytest.fixture(scope="package")
def package_fixture():
    return "package fixture"
