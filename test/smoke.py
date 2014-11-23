from command_will import will

will('list commands', [], output=r"^Available commands:(\n\s*\w+: .*)+$")
will('list settings', ['settings'], output=r"^Current settings:(\n\s*\w+=.* \(.*\))+$")
will('give help on settings', ['help', 'settings'], '')
will('have directory setting', ['--directory=.', 'settings'], output=r"\n  directory=. \(.+\)")
will('list directory contents', ['--directory=.', 'list'], output=r"\bcommander.py\n")
