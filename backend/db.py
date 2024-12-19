from operator import index
import sqlite3
from sqlite3.dbapi2 import Error
import uuid
from sqlalchemy import TEXT, UUID, ForeignKey, create_engine, String, Integer
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    sessionmaker,
)
from sqlalchemy.exc import SQLAlchemyError
from backend.logger.logger import custom_logger
from backend.models.model import PyUser as PyUser


# returns db conn object or None -> needed for crud which was done before sqlalchemy port
def get_db_conn():
    conn = None
    try:
        conn = sqlite3.connect("tododb.db")
    except sqlite3.Error:
        print(f"error connect to database - {Error}")
    finally:
        return conn


# sqlalchemy part
class Base(DeclarativeBase):
    pass


engine = create_engine("sqlite:///test.db", echo=True)
Session = sessionmaker(bind=engine)
session = Session()


class User(Base):
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

    __tablename__ = "user"

    # need to add timestamp of user creation, isdeleted
    # change the names
    # need to change id to uuid

    user_id: Mapped[str] = mapped_column(
        TEXT, primary_key=True, default=lambda: str(uuid.uuid4())
    )
    first_name: Mapped[str] = mapped_column(String)
    last_name: Mapped[str] = mapped_column(String)
    user_name: Mapped[str] = mapped_column(String)
    phone: Mapped[str] = mapped_column(String)
    email: Mapped[str] = mapped_column(String, index=True)
    password: Mapped[str] = mapped_column(String)

    # will do by hand
    # tasks = relationship("Task", back_populates="user", cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return f"id={self.user_id} f_name={self.first_name} l_name={self.last_name} user_name={self.user_name} phone={self.phone} email={self.email}"


class Task(Base):
    """
    task table with the following attributes

    task_id:int -> PK
    task_title:string
    task_description:string
    task_category:string
    user_id:int -> FK to user table

    """

    __tablename__ = "tasksv2"  # This is the table name

    # need to add timestamp of task creation, isdeleted
    # need to change id to uuid

    task_id: Mapped[str] = mapped_column(
        TEXT, primary_key=True, default=lambda: str(uuid.uuid4())
    )
    task_title: Mapped[str] = mapped_column(String, nullable=False)
    task_description: Mapped[str] = mapped_column(String, nullable=False)
    task_category: Mapped[str] = mapped_column(String, nullable=False, index=True)
    user_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("user.user_id"), nullable=False
    )

    # user = relationship("User", back_populates="tasks")

    def __repr__(self) -> str:
        return f"Task(id={self.task_id}, title={self.task_title}, description={self.task_description}, category={self.task_category})"


def create_tables():
    """
    create tables specified by base class - base class is defined in the same module as this function
    returns 0 for sucess or 1 for failure
    """
    try:
        Base.metadata.create_all(engine)

    except SQLAlchemyError as e:
        custom_logger.error(f"exception during table creation {e}")


if __name__ == "__main__":
    create_tables()
