"""
Get help on a specific command such as "settings":
  python commander.py help settings
"""

from command import Command, list_commands, prepare_commands


class Help(Command):
    """Provide help on available commands."""

    subjects = None

    def extract_options(self, command_line):
        self.subjects = command_line
        return []

    def run(self):
        if self.subjects:
            for command in prepare_commands(self.subjects, self.settings):
                print(command.help())
        else:
            print('Available commands:')
            for command_name in list_commands():
                command = prepare_commands([command_name], self.settings)[0]
                try:
                    print('  ' + command.usage())
                except NotImplementedError as e:
                    print(e)
