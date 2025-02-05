class InvalidRouterInstanceException(Exception):
    def __str__(self):
        return "Invalid Router Instance"


class InvalidDescriptionMessagePatternException(Exception):
    def __init__(self, pattern: str):
        self.pattern = pattern
    def __str__(self):
        return ("Invalid Description Message Pattern\n"
                "Correct pattern example: [{command}] *=*=* {description}\n"
                "The pattern must contain two variables: `command` and `description` - description of the command\n"
                f"Your pattern: {self.pattern}")


class OnlyOneMainRouterIsAllowedException(Exception):
    def __init__(self, existing_main_router):
        self.existing_main_router = existing_main_router

    def __str__(self):
        return ("Only One Main Router Allowed\n"
                f"Existing main router is: {self.existing_main_router}")


class MissingMainRouterException(Exception):
    def __str__(self):
        return ("Missing Main Router\n"
                "One of the registered routers must be the main one")
