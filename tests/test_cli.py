from typer.testing import CliRunner
import os
from cli import app

runner = CliRunner()


def test_search():
    start = 3
    end = 5
    TEST_OUTPUT_PATH = "tests/output"
    expected_output = os.path.join(TEST_OUTPUT_PATH, f"{start}-{end}.json")
    os.remove(expected_output)
    assert not os.path.isfile(expected_output)

    result = runner.invoke(
        app,
        ["search", "--start", start, "--end", end, "--output-dir", TEST_OUTPUT_PATH],
    )
    assert result.exit_code == 0
    assert os.path.isfile(expected_output)


def test_tree():
    result = runner.invoke(app, ["print-tree", "5"])

    assert result.exit_code == 0
