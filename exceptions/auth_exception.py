from flask import Response
from werkzeug.exceptions import HTTPException


class AuthException(HTTPException):
    def __init__(self, message):
        super().__init__(
            message,
            Response(
                message,
                401,
                {
                    'WWW-Authenticate': 'Basic realm="Login Required"'
                }
            ))
