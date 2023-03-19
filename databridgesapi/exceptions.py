class HTTPError(Exception):
    pass


class ApiServerError(Exception):
    pass


class TokenScopeError(Exception):
    pass


class ApiNotAuthorizedError(Exception):
    pass


class NotFoundError(Exception):
    pass
