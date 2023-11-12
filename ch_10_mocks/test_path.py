from unittest import mock
from pathlib import Path
import pytest


def home_dir():
    return str(Path.home())


@pytest.fixture
def stub_home_dir():
    # 1st way to patch object
    # with mock.patch("pathlib.Path.home", autospec=True) as stub_home:
    #     yield stub_home

    # 2nd way to patch object
    with mock.patch.object(Path, "home", autospec=True) as stub_home:
        yield stub_home


def test_path_home(stub_home_dir):
    stub_home_dir.return_value = "/users/fake_user"
    assert Path.home() == "/users/fake_user"
