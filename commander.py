#!/usr/bin/env python

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

from configuration.setting import Setting
from configuration.source.environment import Environment
from configuration.source.command_line import CommandLine
from command import run_commands

command_line_configuration = CommandLine()

sources = [
    command_line_configuration,
    Environment(os.environ, 'CMD_')
]

settings_list = [
    Setting("foo", "test", sources)
]

settings = {}

for setting in settings_list:
    settings[setting.name] = setting

command_line = command_line_configuration.extract_settings(settings.keys(), sys.argv[1:])

run_commands(command_line or ['help'], settings)
