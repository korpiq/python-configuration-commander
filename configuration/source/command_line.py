from configuration.source import ConfigurationSource
from getopt import getopt


class CommandLine(ConfigurationSource):
    values = {}

    def extract_settings(self, setting_names, args, option_getter=getopt):
        """
        Extracts values for settings from list of command line arguments.

        :param setting_names: list of names of settings
        :param args: list of command line arguments
        :param option_getter: a function like getopt.getopt
        :return: rest of command line arguments
        """
        option_names = list(map(lambda name: name + '=', setting_names))
        extracted_settings, remaining_args = option_getter(args, '', option_names)

        self.values = {}
        for extracted_setting in extracted_settings:
            extracted_name = extracted_setting[0][2:]  # skip double dash prefix "--"
            value = extracted_setting[1]
            self.values[extracted_name] = value

        return remaining_args

    def get(self, name):
        if name in self.values:
            return self.values[name]
