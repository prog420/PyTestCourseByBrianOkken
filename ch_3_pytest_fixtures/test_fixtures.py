import pytest


@pytest.fixture()
def some_data():
    return 42


def test_some_data(some_data):
    """
    Use fixture to return value in a test.
    """
    assert some_data == 42
