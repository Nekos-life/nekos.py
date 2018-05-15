class NekoException(Exception):
    """ Base exception class for nekos.py """

    pass


class NothingFound(NekoException):
    """ The API didn't return anything """

    pass


class EmptyArgument(NekoException):
    """ When no target is defined """

    pass


class InvalidArgument(NekoException):
    """ Invalid argument within the category """

    pass
