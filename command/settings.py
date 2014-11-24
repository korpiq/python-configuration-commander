from command import Command


class Settings(Command):
    """
    Show currently configured settings.
    """
    def run(self):
        print('Current settings:')
        for setting in self.settings.values():
            print('  ' + setting.description())
