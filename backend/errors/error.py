from abc import ABC, abstractmethod


# Abstract base class for all errors
class CustomError(ABC, Exception):
    """
    Abstract class for errors. All custom errors should inherit from this class.
    """

    @abstractmethod
    def message(self) -> str:
        """Returns the error message."""
        pass


# Specific error classes
class DuplicateUserError(CustomError):
    def message(self) -> str:
        return "User with this email already exists."


class UserNotFound(CustomError):
    def message(self) -> str:
        return "User not found"


# when conversion from Alchemy to Pydantic fails
class AlchemyToPydanticErr(CustomError):
    def message(self) -> str:
        return "AlchemyPydanticConversion failed"


# when conversion from Alchemy to Pydantic fails
class PydanticToAlchemyErr(CustomError):
    def message(self) -> str:
        return "PydanticToAlchemy failed"


class TaskNotFound(CustomError):
    def message(self) -> str:
        return "User not found"
