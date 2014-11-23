"""
Commands inspect or modify target system state as guided by configuration and their own custom options.
"""
from getopt import getopt
import os
import re
import sys


def load_command_class(command_name):
    module_name = 'command.' + command_name
    class_name = command_name[0].upper() + command_name[1:]

    if module_name not in sys.modules:
        try:
            __import__(module_name)
        except ImportError:
            raise InvalidCommandError('Invalid command: "%s"' % command_name)
    try:
        return getattr(sys.modules[module_name], class_name)
    except AttributeError:
        raise NotImplementedError('Command class is not implemented: "%s"' % command_name)


def prepare_commands(command_line, settings):
    prepared_commands = []

    while command_line:
        command_name = command_line.pop(0)
        command_class = load_command_class(command_name)
        command_object = command_class(settings)
        command_line = command_object.extract_options(command_line)
        prepared_commands.append(command_object)

    return prepared_commands


def run_commands(command_line, settings):
    prepared_commands = prepare_commands(command_line, settings)
    for command in prepared_commands:
        command.run()


def list_commands():
    commands = []
    directory = os.path.dirname(__file__)
    for filename in os.listdir(directory):
        match = re.match('^([^\W_]+)\.py$', filename)  # match word letters without underscore
        if match:
            commands.append(match.group(1))
    return commands


class Helpful(object):
    def usage(self):
        try:
            return self.__class__.__name__ + ": " + self.__doc__.strip()
        except AttributeError:
            raise NotImplementedError('Command "%s" is missing usage description' % self.__class__.__name__)

    def help(self):
        try:
            return "\n".join([
                self.usage(),
                '',
                sys.modules[self.__module__].__doc__.strip(),
                ''
            ])
        except AttributeError:
            raise NotImplementedError('Command "%s" is missing documentation' % self.__class__.__name__)


class Command(Helpful):
    options = {}

    def __init__(self, settings):
        self.settings = settings

    def extract_options(self, command_line):
        extracted_options, rest_of_command_line = getopt(command_line, '', list(self.options.keys()))
        self.__handle_options(extracted_options)
        return rest_of_command_line

    def __handle_options(self, options):
        for option in options:
            name = option[0][2:]
            value = option[1]
            self.options[name + '=']['handler'](value)

    def run(self):
        raise NotImplementedError('Command "%s" is not implemented' % self.__class__.__name__)


class InvalidCommandError(ValueError):
    pass
