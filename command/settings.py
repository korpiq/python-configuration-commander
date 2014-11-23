from command import Command


class Settings(Command):
    def run(self):
        print('Current settings:')
        for setting in self.settings.values():
            print('  ' + setting.description())
