commander
=========

Configurable command runner implementation in Python.

This is a template or framework for implementing python programs that take their configuration
from different sources and execute independent commands specified on command line.

Help
----

List available commands with

  ./commander.py
  
Get help with a command with

  ./commander.py help COMMAND

See settings with

  ./commander.py settings

Structure
---------

 * main -- runs each given command with given configuration
 * configuration -- collection of settings from files, command line and environment
 * command -- independently executable commands

Setting
-------

Each configuration setting class can produce settings of that type from given context.

Command
-------

Each command module must contain the following:
 * docstring that provides detailed help for its use
 * one class with
   * same name as containing module but first letter in upper case
   * Command as parent
   * docstring that provides one line description of its use

Optionally each command class may define the following:
 * options: map of option names to { handler: method, purpose: string }
 * run(): run after all options have been handled
 * help(): executed to produce help text for that command.

Tests
-----

Run tests with command

  python test/smoke.py
