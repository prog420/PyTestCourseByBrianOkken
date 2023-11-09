from packaging.version import parse
import pytest
import cards


@pytest.mark.skipif(
    parse(cards.__version__).major < 2,
    reason="Card < comparison is not supported in 1.x",
)
def test_skipif_old_version():
    c1 = cards.Card("task 1")
    c2 = cards.Card("task 2")
    assert c1 < c2
