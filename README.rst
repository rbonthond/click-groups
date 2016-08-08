============
click-groups
============

|build| |license| |coverage|


**This is experimental, which is why it's not on PyPI**

Add (groups) to a list of click_ group commands.

In your click_ app:

.. code:: python

    import click
    from click_groups import ClickCommandGroup

    @click.group(cls=ClickAliasedGroup)
    def cli():
        pass

    @cli.command(group=['group1', 'group2'])
    def foo():
        """Run a command."""
        click.echo('foo')

Will result in:

.. code::

    Usage: cli [OPTIONS] COMMAND [ARGS]...

    Options:
      --help  Show this message and exit.

    Group1 commands:
      foo   Run a command.

    Group2 commands:
      foo   Run a command.


.. _click: http://click.pocoo.org/

.. |build|  image:: https://travis-ci.org/rbonthond/click-groups.svg?branch=master
    :target: https://travis-ci.org/rbonthond/click-groups
    :alt: Build status of the master branch

.. |license| image:: https://img.shields.io/badge/license-MIT-blue.svg?style=flat
    :target: https://raw.githubusercontent.com/rbonthond/click-groups/master/LICENSE
    :alt: Package license

.. |coverage| image:: https://coveralls.io/repos/github/rbonthond/click-groups/badge.svg?branch=master
    :target: https://coveralls.io/github/rbonthond/click-groups?branch=master
    :alt: Coverage report
