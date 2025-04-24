from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from fastapi import Depends, HTTPException, status

from backend.api.utils.db_collection import mongodb
from backend.api.utils.hash_password import SECRET_KEY, ALGORITHM, pwd_context

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/user/api/v1/login")


async def authenticate_user(username: str, password: str):
    user = await mongodb["users"].find_one({"username": username})
    if not user or not pwd_context.verify(password, user["password"]):
        return False
    return user


async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        return username
    except JWTError:
        raise credentials_exception