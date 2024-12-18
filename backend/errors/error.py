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
