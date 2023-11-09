import pytest
from cards import Card


# @pytest.fixture(params=["done", "in prog", "todo"])
# def state(request):
#     """
#     Fixture will be called three times, once for each value in params.
#     """
#     print(f" State: {request.param} setup ")
#     yield request.param
#     print(f" State: {request.param} teardown ")


def test_state(cards_db, state):
    c = Card("write a book", state=state)
    index = cards_db.add_card(c)
    cards_db.finish(index)
    card = cards_db.get_card(index)
    assert card.state == "done"
