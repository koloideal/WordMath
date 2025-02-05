class InvalidCommandInstanceException(Exception):
    def __str__(self):
        return "Invalid Command Instance"


class InvalidDescriptionInstanceException(Exception):
    def __str__(self):
        return "Invalid Description Instance"


class UnknownCommandHandlerHasAlreadyBeenCreatedException(Exception):
    def __str__(self):
        return "Unknown Command Handler has already been created"
