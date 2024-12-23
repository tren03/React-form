from sqlalchemy import (Boolean, DateTime, Engine, ForeignKey, Integer, String,
                        func)
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from backend.db.db_connection import get_engine


# sqlalchemy part
class Base(DeclarativeBase):
    pass


class UserModel(Base):
    """
    User table with the following attributes

    id:int -> PK
    first_name:string
    last_name:string
    user_name:string
    phone:string
    email:string
    password:string

    """

    __tablename__: str = "user"

    user_id: Mapped[str] = mapped_column(String, primary_key=True)
    first_name: Mapped[str] = mapped_column(String)
    last_name: Mapped[str] = mapped_column(String)
    user_name: Mapped[str] = mapped_column(String)
    phone: Mapped[str] = mapped_column(String)
    email: Mapped[str] = mapped_column(String, index=True)
    password: Mapped[str] = mapped_column(String)
    time_created: Mapped[DateTime] = mapped_column(DateTime, server_default=func.now())
    time_updated: Mapped[DateTime] = mapped_column(
        DateTime, server_default=func.now(), onupdate=func.now()
    )
    is_deleted: Mapped[bool] = mapped_column(Boolean, default=False)

    # will do by hand
    # tasks = relationship("Task", back_populates="user", cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return f"id={self.user_id} f_name={self.first_name} l_name={self.last_name} user_name={self.user_name} phone={self.phone} email={self.email}"


class TaskModel(Base):
    """
    task table with the following attributes

    task_id:int -> PK
    task_title:string
    task_description:string
    task_category:string
    user_id:str -> FK to user table

    """

    __tablename__: str = "tasksv2"  # This is the table name

    task_id: Mapped[str] = mapped_column(String, primary_key=True)
    task_title: Mapped[str] = mapped_column(String, nullable=False)
    task_description: Mapped[str] = mapped_column(String, nullable=False)
    task_category: Mapped[str] = mapped_column(String, nullable=False, index=True)
    user_id: Mapped[str] = mapped_column(
        Integer, ForeignKey("user.user_id"), nullable=False
    )
    time_created: Mapped[DateTime] = mapped_column(DateTime, server_default=func.now())
    time_updated: Mapped[DateTime] = mapped_column(
        DateTime, server_default=func.now(), onupdate=func.now()
    )
    is_deleted: Mapped[bool] = mapped_column(Boolean, default=False)
    # user = relationship("User", back_populates="tasks")

    def __repr__(self) -> str:
        return f"Task(id={self.task_id}, title={self.task_title}, description={self.task_description}, category={self.task_category})"


def create_tables(engine: Engine) -> int:
    """
    create tables specified by base class - base class is defined in the same module as this function
    returns 0 for sucess or 1 for failure
    """
    try:
        Base.metadata.create_all(engine)
    except SQLAlchemyError as e:
        print(f"exception during table creation {e}")
        return 1
    return 0


if __name__ == "__main__":
    _ = create_tables(get_engine())
