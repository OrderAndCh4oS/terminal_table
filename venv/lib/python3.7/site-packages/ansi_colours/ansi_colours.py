# coding=utf-8


class AnsiColours:
    colours = {
        'black': '\033[0;30m',
        'blue': '\033[0;34m',
        'cyan': '\033[0;36m',
        'green': '\033[0;32m',
        'red': '\033[0;31m',
        'purple': '\033[0;35m',
        'yellow': '\033[0;33m',
        'light_grey': '\033[0;37m',
        'colour_end': '\033[0m'
    }

    @classmethod
    def black(cls, text):
        return cls.colours['black'] + text + cls.colours['colour_end']

    @classmethod
    def blue(cls, text):
        return cls.colours['blue'] + text + cls.colours['colour_end']

    @classmethod
    def cyan(cls, text):
        return cls.colours['cyan'] + text + cls.colours['colour_end']

    @classmethod
    def green(cls, text):
        return cls.colours['green'] + text + cls.colours['colour_end']

    @classmethod
    def red(cls, text):
        return cls.colours['red'] + text + cls.colours['colour_end']

    @classmethod
    def purple(cls, text):
        return cls.colours['purple'] + text + cls.colours['colour_end']

    @classmethod
    def yellow(cls, text):
        return cls.colours['yellow'] + text + cls.colours['colour_end']

    @classmethod
    def light_grey(cls, text):
        return cls.colours['light_grey'] + text + cls.colours['colour_end']
