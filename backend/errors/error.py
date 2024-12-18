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


# for login when email not found
class EmailNotFoundErr(CustomError):
    def message(self) -> str:
        return "User email not found during login"


# when conversion from Alchemy to Pydantic fails
class AlchemyToPydanticErr(CustomError):
    def message(self) -> str:
        return "AlchemyPydanticConversion failed"


# when conversion from Alchemy to Pydantic fails
class PydanticToAlchemyErr(CustomError):
    def message(self) -> str:
        return "PydanticToAlchemy failed"
