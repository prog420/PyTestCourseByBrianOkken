import pytest
from cards import CardsDB


@pytest.fixture()
def cards_db(tmp_path):
    db = CardsDB(tmp_path)
    yield db
    # Teardown
    db.close()


@pytest.fixture(params=["done", "in prog", "todo"])
def state(request):
    """
    Fixture will be called three times, once for each value in params.
    """
    print(f" State: {request.param} setup ")
    yield request.param
    print(f" State: {request.param} teardown ")
