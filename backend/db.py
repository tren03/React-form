import sqlite3
from sqlite3.dbapi2 import Error
from sqlalchemy import ForeignKey, create_engine, String, Integer
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    relationship,
    sessionmaker,
)
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from backend.model import User as PyUser


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


engine = create_engine("sqlite:///tododb.db", echo=True)
Session = sessionmaker(bind=engine)
session = Session()


class User(Base):
    """
    User table with the following attributes

    id:int -> PK
    f_name:string
    l_name:string
    user_name:string
    phone:string
    email:string
    password:string

    """

    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    f_name: Mapped[str] = mapped_column(String)
    l_name: Mapped[str] = mapped_column(String)
    user_name: Mapped[str] = mapped_column(String)
    phone: Mapped[str] = mapped_column(String)
    email: Mapped[str] = mapped_column(String)
    password: Mapped[str] = mapped_column(String)

    tasks = relationship("Task", back_populates="user", cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return f"id={self.id} f_name={self.f_name} l_name={self.l_name} user_name={self.user_name} phone={self.phone} email={self.email}"


class Task(Base):
    """
    task table with the following attributes

    taskId:int -> PK
    taskTitle:string
    taskDescription:string
    taskCategory:string
    user_id:int -> FK to user table

    """

    __tablename__ = "tasksv2"  # This is the table name

    taskId: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    taskTitle: Mapped[str] = mapped_column(String, nullable=False)
    taskDescription: Mapped[str] = mapped_column(String, nullable=False)
    taskCategory: Mapped[str] = mapped_column(String, nullable=False)

    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("user.id"), nullable=False)
    user = relationship("User", back_populates="tasks")

    def __repr__(self) -> str:
        return f"Task(id={self.taskId}, title={self.taskTitle}, description={self.taskDescription}, category={self.taskCategory})"


def create_tables() -> int:
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


def add_user(user_to_add: PyUser) -> int:
    """
    Adds a user to the "user" table
    Accepts a pydantic user model and adds in to the database by converting to sqlalchemy model
    returns
    0 = success
    1 = IntegrityError -> duplicate user addition
    2 = general error
    """
    try:
        if session.query(User).filter(User.email == user_to_add.email).first():
            # we have a existing user
            print("existing user addition error")
            return 1
        sql_alchemy_user_to_add = User(
            f_name=user_to_add.f_name,
            l_name=user_to_add.l_name,
            user_name=user_to_add.user_name,
            phone=user_to_add.phone,
            email=user_to_add.email,
            password=user_to_add.password,
        )
        session.add(sql_alchemy_user_to_add)
        session.commit()


    except SQLAlchemyError as e:
        print(f"exception during user creation {e}")
        return 2
    return 0


if __name__ == "__main__":
    create_tables()
