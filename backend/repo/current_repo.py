from backend.conversions.conversion_interface import IConversion
from backend.conversions.sqlite_conversions import SqliteConversion
from backend.db.db_connection import get_session
from backend.repo.repo_interface import IRepo
from backend.repo.sqlite_repo import SqliteRepo


def get_repo() -> IRepo:
    converter: IConversion = SqliteConversion()
    repo: IRepo = SqliteRepo(converter, get_session())
    return repo
