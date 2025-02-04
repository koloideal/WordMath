class InvalidCommandInstanceException(Exception):
    def __str__(self):
        return "Invalid Command Instance"


class UnknownCommandHandlerHasAlreadyBeenCreatedException(Exception):
    def __str__(self):
        return "Unknown Command Handler has already been created"
