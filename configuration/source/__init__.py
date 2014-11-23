"""
Configuration Sources provide values for Configuration Settings.
"""


class ConfigurationSource(object):
    def get(self, name):
        raise NotImplemented('Configuration source "%s" not implemented' % self.__class__.__name__)
