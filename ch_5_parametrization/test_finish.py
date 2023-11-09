import pytest
from cards import Card


def test_finish_from_in_prog(cards_db):
    index = cards_db.add_card(Card("second ed", state="in prog"))
    cards_db.finish(index)
    card = cards_db.get_card(index)
    assert card.state == "done"


def test_finish_from_done(cards_db):
    index = cards_db.add_card(Card("second ed", state="done"))
    cards_db.finish(index)
    card = cards_db.get_card(index)
    assert card.state == "done"


def test_finish_from_todo(cards_db):
    index = cards_db.add_card(Card("second ed", state="todo"))
    cards_db.finish(index)
    card = cards_db.get_card(index)
    assert card.state == "done"


@pytest.mark.parametrize("summary, status", [
    ("write a book", "done"),
    ("second edition", "in prog"),
    ("create a course", "todo"),
])
def test_finish_from_status(summary, status, cards_db):
    index = cards_db.add_card(Card(summary, state=status))
    cards_db.finish(index)
    card = cards_db.get_card(index)
    assert card.state == "done"
