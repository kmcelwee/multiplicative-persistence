from typer.testing import CliRunner

from cli import app

runner = CliRunner()


def test_app():
    result = runner.invoke(app, ["--start", "3", "--end", "5"])
    assert result.exit_code == 0
