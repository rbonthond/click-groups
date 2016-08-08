import click
from click.testing import CliRunner
from click_groups import ClickCommandGroup
import pytest


@pytest.fixture(scope="function")
def runner():
    return CliRunner()


@click.group(cls=ClickCommandGroup)
def cli():
    pass


@cli.command()
def foo():
    """Run a command."""
    click.echo('foo')


TEST_HELP = """Usage: cli [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  foo  Run a command.
"""


def test_help(runner):
    result = runner.invoke(cli)
    assert result.output == TEST_HELP


def test_foobar(runner):
    result = runner.invoke(cli, ['foo'])
    assert result.output == 'foo\n'


TEST_INVALID = """Usage: cli [OPTIONS] COMMAND [ARGS]...

Error: No such command "bar".
"""


def test_invalid(runner):
    result = runner.invoke(cli, ['bar'])
    assert result.output == TEST_INVALID
