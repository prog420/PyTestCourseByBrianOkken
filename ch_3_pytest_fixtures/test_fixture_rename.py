import pytest


@pytest.fixture(name="ultimate_answer")
def _ultimate_answer():
    return 42


def test_answer(ultimate_answer):
    assert ultimate_answer == 42
