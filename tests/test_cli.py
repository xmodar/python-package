"""Unit testing for python_package.cli."""

from click.testing import CliRunner

from python_package.cli import main


def test_meanings():
    """Test python_package.cli.meanings."""
    runner = CliRunner()
    result = runner.invoke(main, ['meanings', 'friend'])
    assert result.exit_code == 0
    assert result.output


def test_suggestions():
    """Test python_package.cli.suggestions."""
    runner = CliRunner()
    result = runner.invoke(main, ['suggestions', 'friend'])
    assert result.exit_code == 0
    assert result.output
