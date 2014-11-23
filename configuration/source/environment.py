from configuration.source import ConfigurationSource


class Environment(ConfigurationSource):
    def __init__(self, environment, prefix=''):
        self.environment = environment
        self.prefix = prefix

    def get(self, name):
        env_name = self.prefix + name.upper()
        if env_name in self.environment:
            return self.environment[env_name]
