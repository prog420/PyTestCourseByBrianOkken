from unittest import mock
import subprocess
import pytest
import cards


def test_mock_CardsDB():
    """
    Test to check if we have the mocking setup right.
    :return:
    """
    with mock.patch.object(cards, "CardsDB") as MockCardsDB:
        print()
        print(f"   class: {MockCardsDB}")
        print(f"return_value: {MockCardsDB.return_value}")
        with cards.cli.cards_db() as db:
            print(f"   object: {db}")


def test_unittest_mock_db(tmp_path):
    """
    1. Mocking database using unittest.mock.
    2. Changing behaviour when someone calls path() or count().
    """
    # Create mock object
    # (obj needed for the tests
    # could be obtained from MockCardsDB.return_value)
    with mock.patch.object(cards, "CardsDB") as MockCardsDB:
        # Set required return values
        MockCardsDB.return_value.path.return_value = "/foo"
        MockCardsDB.return_value.count.return_value = 100
        # Act (with created mock) and assert
        with cards.cli.cards_db() as db:
            print(f"\n{db}")
            print(f"dp.path(): {db.path()}")
            card = cards.Card("mock card", "brian", "todo", 123)
            db.add_card(card)
            print(f"db.count(): {db.count()}")
            assert db.count() == 100


""" 2. Converting mock function to a fixture """


@pytest.fixture()
def mock_cardsdb():
    # 1st way to mock object
    # cards.CardsDB = mock.Mock()
    # return cards.CardsDB.return_value

    # 2nd way to mock object
    with mock.patch.object(cards, "CardsDB", autospec=True) as MockCardsDB:
        yield MockCardsDB.return_value


def test_config(mock_cardsdb, capsys):
    """
    Test to check mocked db fixture
    """
    mocked_path = "/foo/"
    mock_cardsdb.path.return_value = mocked_path
    cards.cli.config()
    output = capsys.readouterr().out.rstrip()
    assert output == mocked_path


def test_assert_called_with(mock_cardsdb):
    """
    Making sure functions are called correctly.
    Example:
    ...
    E AssertionError: expected call not found.
    E Expected: add_card(Card(summary='some task', owner='Brian', ...
    E Actual: add_card(Card(summary='some task', owner='brian', ...
    ...
    """
    cards.cli.add(summary=["some task"], owner="brian")
    expected = cards.Card("some task", owner="brian", state="todo")
    mock_cardsdb.add_card.assert_called_with(expected)
