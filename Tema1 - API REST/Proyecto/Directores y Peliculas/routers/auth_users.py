from pydantic import BaseModel

from datetime import *
import jwt
from jwt.exceptions import InvalidTokenError
from pwdlib import PasswordHash
from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer

# OAuth2PasswordRequestForm envia usuario y contraseña.

# Algoritmo de cifrado del token.
ALGORITHM = "HS256"

# Tiempo de expiración del token.
ACCESS_TOKEN_EXPIRE_MINUTES = 5

# Clave cifrado del token.
SECRET_KEY = "56a399d47727accfdbc921b5f9940f1d9f8e248e1689b7564596778d9847d53d"


# Objeto para cifrar la contraseña.
password_hash = PasswordHash.recommended()

# Se encarga de realizar la autenticación.
oauth2 = OAuth2PasswordBearer(tokenUrl="login")

router = APIRouter()


class User(BaseModel):
    username: str
    fullname: str
    email: str
    disabled: bool


class UserDB(User):
    password: str


users_db = {
    "pabloip": {
        "username": "pablo.iglesias",
        "fullname": "Pablo Iglesias Prieto",
        "email": "pablo.iglesias@iesnervion.es",
        "disabled": False,
        "password": "123",
    },
    "admin": {
        "username": "admin",
        "fullname": "admin",
        "email": "admin@iesnervion.es",
        "disabled": False,
        "password": "admin",
    },
    "pepito": {
        "username": "pepito.grillo",
        "fullname": "Pepito Grillo",
        "email": "pepito.grillo@iesnervion.es",
        "disabled": False,
        "password": "$argon2id$v=19$m=65536,t=3,p=4$tohgbnX58smJFon5vTyRIg$abip3TANfwUo8Gqp2zp54DXqbc8mrmopGsMicrKiAsA",
    },
}


@router.post("/register", status_code=201)
def register(user: UserDB):
    if user.username not in users_db:
        hashed_password = password_hash.hash(user.password)
        user.password = hashed_password
        users_db[user.username] = user
        return user
    raise HTTPException(status_code=409, detail="The user already exists")

@router.post("/login", status_code=201)
async def login(form:OAuth2PasswordRequestForm = Depends()):
    # Cogemos el usuario.
    username = users_db.get(form.username)
    
    if username:
        #Si el usuario existe en la bbdd.
        # Comprobamos las contraseñas.
        if password_hash.verify(form.password, username["password"]):
            expire = datetime.now(timezone.utc) + timedelta(minutes = ACCESS_TOKEN_EXPIRE_MINUTES)
            access_token = {"sub" : form.username}
            token = jwt.encode(access_token, SECRET_KEY, algorithm=ALGORITHM)
            return {"access token" : token, "token type" : "bearer" }
    raise HTTPException(status_code=401, detail="Usuario o contraseña incorrecta")
    