from typing import LiteralString

from .reason import ErrorReason


class ErrorMessageFactory:
    """
    The ErrorMessageFactory is a factory class that standardized messages for RequestError message field.
    """
    def get_row(self, reason: str) -> str:
        """
        return unformatted str message for RequestError or his child classes.

        Check out all message formats:
            - EMPTY -> "{} is empty or null."
            - JSON_FORMAT -> "Invalid JSON format."
            - PATTERN -> "{} can only consist these characters: {}"
            - BAD_UUID -> "Invalid UUID format."
            - BAD_DATA_TYPE -> "{} has invalid data type."
            - NOT_SUIT  -> "{} doesn't suit. Suitable values: {}."
            - NOT_EQUAL  -> "{} is not equal to {}."
            - NOT_EXIST  -> "{} doesn't exist."
            - EXIST  -> "{} already exist."
            - NOT_MATCH  -> "{} doesn't match."
            - SCOPE -> "This {} has {} scope, which doesn't allow you."
            - OWNER_ACCESS -> "You don't have access for this request, because you are not the owner of this {}."
            - LESS_SIZE -> "{} can't have value less than {}."
            - GREATER_SIZE -> "{} can't have value greater than {}."
            - NOT_ALLOW -> "{} isn't allow for this user."
            - ENCRYPTION -> "Encrypted data isn't valid."
        """
        match reason:
            case ErrorReason.EMPTY.name:
                return "{} is empty or null."
            case ErrorReason.JSON_FORMAT.name:
                return "Invalid JSON format."
            case ErrorReason.PATTERN.name:
                return "{} can only consist these characters: {}"
            case ErrorReason.BAD_UUID.name:
                return "Invalid UUID format."
            case ErrorReason.BAD_DATA_TYPE.name:
                return "{} has invalid data type."
            case ErrorReason.NOT_SUIT.name:
                return "{} doesn't suit. Suitable values: {}."
            case ErrorReason.NOT_EQUAL.name:
                return "{} is not equal to {}."
            case ErrorReason.NOT_EXIST.name:
                return "{} doesn't exist."
            case ErrorReason.EXIST.name:
                return "{} already exist."
            case ErrorReason.NOT_MATCH.name:
                return "{} doesn't match."
            case ErrorReason.SCOPE.name:
                return "This {} has {} scope, which doesn't allow you."
            case ErrorReason.OWNER_ACCESS.name:
                return "You don't have access for this request, because you are not the owner of this {}."
            case ErrorReason.LESS_SIZE.name:
                return "{} can't have value less than {}."
            case ErrorReason.GREATER_SIZE.name:
                return "{} can't have value greater than {}."
            case ErrorReason.NOT_ALLOW.name:
                return "{} isn't allow for this user."
            case ErrorReason.ENCRYPTION.name:
                return "Encrypted data isn't valid."
            case _:
                raise ValueError

    def get(self, reason: str, *params: LiteralString) -> str:
        """return formatted clean str message for RequestError or his child classes."""
        return self.get_row(reason).format(*params)