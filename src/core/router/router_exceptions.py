class InvalidCommandInstanceException(Exception):
    def __str__(self):
        return "Invalid Command Instance"