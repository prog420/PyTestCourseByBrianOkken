import pytest
from cards import Card


def pytest_generate_tests(metafunc: pytest.Metafunc):
    print(f"\nMetafunc for {metafunc.function}")
    print(f"Fixtures for {metafunc.function}: {metafunc.fixturenames}")
    if "state_hook_test" in metafunc.fixturenames:
        metafunc.parametrize("state_hook_test", ["done", "in prog", "todo"])


def test_hook_pytest_generate_tests(cards_db, state_hook_test):
    c = Card("write a book", state=state_hook_test)
    index = cards_db.add_card(c)
    cards_db.finish(index)
    card = cards_db.get_card(index)
    assert card.state == "done"
