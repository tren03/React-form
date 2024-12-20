import jwt
from datetime import datetime, timedelta
from backend.models.dto import JWTInfo


# Secret key to sign the JWT (will move to .env after testing)
SECRET_KEY = "somuchsecretwow"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_jwt(jwt_info: JWTInfo):
    data = vars(jwt_info)
    expire_delta: timedelta = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    expire = datetime.now() + expire_delta
    data["exp"] = expire
    print(data)

    pass


def verify_jwt():
    pass
