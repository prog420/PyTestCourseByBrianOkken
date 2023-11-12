import subprocess
import pytest
import cards


def monkeypatch_version():
    print("monkeypatched_version")


@pytest.fixture()
def cards_db(tmp_path):
    db = cards.CardsDB(tmp_path)
    yield db
    # Teardown
    db.close()


def test_monkeypatch_version(monkeypatch, capsys):
    # Replace version func with monkeypatched version
    monkeypatch.setattr("cards.cli.version", monkeypatch_version)
    # Call monkeypatched version and read output
    cards.cli.version()
    output = capsys.readouterr().out.rstrip()
    # Check output
    assert output == "monkeypatched_version"
