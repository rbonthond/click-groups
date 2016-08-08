"""
    Extension for the python ``click`` module
    to provide a grouping for a list of command groups.
"""

from collections import defaultdict
import click


class ClickCommandGroup(click.Group):
    def __init__(self, *args, **kwargs):
        super(ClickCommandGroup, self).__init__(*args, **kwargs)
        self._groups = {}

    def command(self, *args, **kwargs):
        groups = kwargs.pop('groups', [])
        decorator = super(ClickCommandGroup, self).command(*args, **kwargs)
        if not groups:
            return decorator

        def _decorator(f):
            cmd = decorator(f)
            self._groups[cmd.name] = groups
            return cmd

        return _decorator

    def format_commands(self, ctx, formatter):
        groups = defaultdict(list)
        for sub_command in self.list_commands(ctx):
            cmd = self.get_command(ctx, sub_command)
            if cmd is None:
                continue
            if hasattr(cmd, 'hidden') and cmd.hidden:
                continue
            cmd_help = cmd.short_help or ''
            if self._groups:
                for group in self._groups[sub_command]:
                    groups[group].append((sub_command, cmd_help))
            else:
                groups[''].append((sub_command, cmd_help))
        for group in sorted(groups.keys()):
            if group == '':
                title = 'Commands'
            else:
                title = '{} commands'.format(group.title())
            with formatter.section(title):
                formatter.write_dl(groups[group])
