import click
from click_groups import ClickCommandGroup


@click.group(cls=ClickCommandGroup)
def cli():
    pass


@cli.command(groups=['foo', 'bar'])
def foo():
    """Run a command."""
    click.echo('foo')


if __name__ == "__main__":
    cli()
