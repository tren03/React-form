import sqlite3
from sqlite3.dbapi2 import Error
from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import sessionmaker, Session


DB_URL = "sqlite:///test.db"


# returns db conn object or None -> needed for crud which was done before sqlalchemy port
def get_db_conn():
    conn = None
    try:
        conn = sqlite3.connect("tododb.db")
    except sqlite3.Error:
        print(f"error connect to database - {Error}")
    finally:
        return conn


def get_session() -> Session:
    engine = create_engine(DB_URL, echo=False)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session


def get_engine() -> Engine:
    engine = create_engine(DB_URL, echo=False)
    return engine
