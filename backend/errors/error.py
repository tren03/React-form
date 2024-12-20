from abc import ABC, abstractmethod


# Abstract base class for all errors
class CustomError(ABC, Exception):
    """
    Abstract class for errors. All custom errors should inherit from this class.
    """

    @abstractmethod
    def message(self) -> str:
        """Returns the error message."""


# Specific error classes
class DuplicateUserError(CustomError):
    def message(self) -> str:
        return "User with this email already exists."


# Specific error classes
class InvalidUserLogin(CustomError):
    def message(self) -> str:
        return "Invalid login credentaials"


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
        return "task not found"


# Error for UserEntity to UserModel conversion
class UserEntityToUserModelConversionError(CustomError):
    def message(self) -> str:
        return "Couldn't convert UserEntity to UserModel"


# Error for TaskEntity to TaskModel conversion
class TaskEntityToTaskModelConversionError(CustomError):
    def message(self) -> str:
        return "Couldn't convert TaskEntity to TaskModel"


# Error for UserModel to UserEntity conversion
class UserModelToUserEntityConversionError(CustomError):
    def message(self) -> str:
        return "Couldn't convert UserModel to UserEntity"


# Error for TaskModel to TaskEntity conversion
class TaskModelToTaskEntityConversionError(CustomError):
    def message(self) -> str:
        return "Couldn't convert TaskModel to TaskEntity"


# Error for UserDto to UserEntity conversion
class UserDtoToUserEntityConversionError(CustomError):
    def message(self) -> str:
        return "Couldn't convert UserDto to UserEntity"


# Error for TaskDto to TaskEntity conversion
class TaskDtoToTaskEntityConversionError(CustomError):
    def message(self) -> str:
        return "Couldn't convert TaskDto to TaskEntity"


# Error for UserEntity to UserDto conversion
class UserEntityToUserDtoConversionError(CustomError):
    def message(self) -> str:
        return "Couldn't convert UserEntity to UserDto"


# Error for TaskEntity to TaskDto conversion
class TaskEntityToTaskDtoConversionError(CustomError):
    def message(self) -> str:
        return "Couldn't convert TaskEntity to TaskDto"


# Error for SiginInDto to TaskDto conversion
class UserSignInDtoToUserEntityConversionError(CustomError):
    def message(self) -> str:
        return "Couldn't convert TaskEntity to TaskDto"


# Error for invalid or expired JWT
class InvalidJWT(CustomError):
    def message(self) -> str:
        return "Couldn't convert TaskEntity to TaskDto"
