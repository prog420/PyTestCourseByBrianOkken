from tempfile import TemporaryDirectory
from pathlib import Path
import cards
import pytest

""" Dynamic Scope: pass Callable instead of string. """


def db_scope(fixture_name, config):
    print(f"Fixture name: {fixture_name}")
    if config.getoption("--func-db", None):
        return "function"
    return "session"


"""Using Multiple Fixture Levels (example: database cleaning)"""


@pytest.fixture(scope="session")
def some_cards():
    """ List of different Card objects """
    return [
        cards.Card("write book", "Brian", "done"),
        cards.Card("edit book", "Katie", "done"),
        cards.Card("write 2nd edition", "Brian", "todo"),
        cards.Card("edit 2nd edition", "Katie", "todo"),
    ]


@pytest.fixture(scope=db_scope)
def db():
    """CardsDB object connected to a temporary database"""
    with TemporaryDirectory() as db_dir:
        # Setup
        db_path = Path(db_dir)
        db_ = cards.CardsDB(db_path)
        yield db_
        # Teardown
        db_.close()


@pytest.fixture(scope="function")
def cards_db(db):
    """ CardsDB object that's empty """
    db.delete_all()
    return db


@pytest.fixture(scope="function")
def non_empty_db(cards_db, some_cards):
    """ CardsDB object that's been populated with some cards """
    for c in some_cards:
        cards_db.add_card(c)
    return cards_db


def test_two(cards_db):
    cards_db.add_card(cards.Card("first"))
    cards_db.add_card(cards.Card("second"))
    assert cards_db.count() == 2


def test_three(cards_db):
    cards_db.add_card(cards.Card("first"))
    cards_db.add_card(cards.Card("second"))
    cards_db.add_card(cards.Card("three"))
    assert cards_db.count() == 3


def test_add_some(cards_db, some_cards):
    expected_count = len(some_cards)
    for c in some_cards:
        cards_db.add_card(c)
    assert cards_db.count() == expected_count


def test_non_empty_db(non_empty_db):
    assert non_empty_db.count() > 0
