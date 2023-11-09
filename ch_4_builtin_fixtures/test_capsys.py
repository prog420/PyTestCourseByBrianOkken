import sys
import subprocess
import cards


def test_output_subprocess():
    process = subprocess.run(
        ["cards", "version"], capture_output=True, text=True
    )
    output = process.stdout.rstrip()
    assert output == cards.__version__


def test_capsys_out(capsys):
    # print("output")
    # sys.stdout.write("output")
    sys.stderr.write("output")
    output = capsys.readouterr().out.rstrip()
    assert output == "output"


def test_capsys_err(capsys):
    sys.stderr.write("err")
    output = capsys.readouterr().err.rstrip()
    assert output == "err"
