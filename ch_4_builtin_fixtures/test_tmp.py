
def test_tmp_path(tmp_path):
    file = tmp_path / "file.txt"
    file.write_text("Hello")
    print(f"File: {file}")
    assert file.read_text() == "Hello"


def test_tmp_path_factory(tmp_path_factory):
    path = tmp_path_factory.mktemp("sub")
    print(f"Path: {path}")
    file = path / "file.txt"
    print(f"File: {file}")
    file.write_text("Hello")
    assert file.read_text() == "Hello"
