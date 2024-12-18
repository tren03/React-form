from backend.db.user_operations import get_user_by_email
from backend.errors.error import EmailNotFoundErr
from backend.models.model import LoginDetails


# should return jwt for user, for now returning None
def verify_login(obj: LoginDetails) -> bool:
    """
    We check if the email and password exist in the database and are valid
    """
    stat = get_user_by_email(obj.email)
    if isinstance(stat, Exception):
        return False
    if obj.password == stat.password:
        return True
    return False
