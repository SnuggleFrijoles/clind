

class ClindException(Exception):
    """
    class: ClindException

    An abstract exception type for all clind exceptions
    """

    def __init__(self, message):

        self.message = message

