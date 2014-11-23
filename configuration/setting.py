"""
Provides abstract base class for configuration settings.
"""


class Setting:

    def __init__(self, name, purpose, sources):
        self.name = name
        self.purpose = purpose
        self.sources = sources

    def value(self):
        for source in self.sources:
            value = source.get(self.name)
            if value is not None:
                return value

    def __str__(self):
        return str(self.value())

    def description(self):
        return "%s=%s (%s)" % (self.name, str(self), self.purpose)
