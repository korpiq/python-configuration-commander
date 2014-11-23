from command_will import will

commands_match = r"Available commands:(\n\s*\w+: .*)+"
settings_match = r"Current settings:(\n\s*\w+=.* \(.*\))+"

will('list commands', [], output="^" + commands_match + "$")
will('list settings', ['settings'], output="^" + settings_match + "$")
will('list settings and commands', ['settings', 'help'], output="^" + settings_match + "\n" + commands_match + "$")

will('give help on settings', ['help', 'settings'])
will('have directory setting', ['--directory=.', 'settings'], output=r"\n\s*directory=. \(.+\)")
will('list directory contents', ['--directory=.', 'list'], output=r"\bcommander.py\n")
