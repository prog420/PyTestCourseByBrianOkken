import pytest
from cards import Card

# File-level marker.
# pytestmark = pytest.mark.skip


class TestPytestMark:
    def test_one(self, request: pytest.FixtureRequest):
        print(f"Node ID: {request.node.nodeid}")
        assert 1 == 1

    def test_two(self, request: pytest.FixtureRequest):
        print(f"Node ID: {request.node.nodeid}")
        assert 2 == 2
