from enum import Enum

class ErrorReason(Enum):
    """The ErrorReason is an enum, that points on one of the reason of error for 4xx response status."""
    EMPTY = 0
    JSON_FORMAT = 1
    PATTERN = 2
    BAD_UUID = 3
    BAD_DATA_TYPE = 4
    NOT_SUIT = 5
    NOT_EQUAL = 6
    NOT_EXIST = 7
    EXIST = 8
    NOT_FOUND = 9
    NOT_MATCH = 10
    SCOPE = 11
    OWNER_ACCESS = 12
    LESS_SIZE = 13
    GREATER_SIZE = 14
    NOT_ALLOW = 15
    ENCRYPTION = 16