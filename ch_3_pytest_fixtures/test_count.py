from tempfile import TemporaryDirectory
from pathlib import Path
import cards
import pytest


@pytest.fixture()
def cards_db():
    with TemporaryDirectory() as db_dir:
        # Setup
        db_path = Path(db_dir)
        db = cards.CardsDB(db_path)
        print(f"\nPath: {db_path}\n")
        yield db
        # Teardown
        db.close()


def test_empty(cards_db):
    assert cards_db.count() == 0


def test_two_cards(cards_db):
    cards_db.add_card(cards.Card("first"))
    cards_db.add_card(cards.Card("second"))
    assert cards_db.count() == 2
