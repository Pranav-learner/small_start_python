class UserAlreadyExists(Exception):
    pass


class InvalidCredentials(Exception):
    pass


class InvalidToken(Exception):
    pass

class Forbidden(Exception):
    pass


class UserNotFound(Exception):
    pass