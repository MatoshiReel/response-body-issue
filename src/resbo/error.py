from typing import LiteralString

from .issue import RequestIssue
from .message import ErrorMessageFactory


class RequestError(RequestIssue):
    """The RequestError is a DTO class, that describes a reason of error for 4xx response status."""
    errorReason: str

    def system_message(self, *params: LiteralString):
        if len(params) == 0:
            self.message = ErrorMessageFactory().get_row(self.errorReason)
        else:
            self.message = ErrorMessageFactory().get(self.errorReason, *params)
        return self

class RequestFieldError(RequestError):
    field: str

class RequestParamError(RequestError):
    param: str
