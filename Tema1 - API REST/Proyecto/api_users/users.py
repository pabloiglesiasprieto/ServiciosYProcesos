from fastapi import FastAPI
from pydantic import BaseModel


# DIRECTOR (Id, DNI, Nombre, Apellidos, Nacionalidad)
class Director(BaseModel):
    id: int
    dni: str
    name: str
    apellidos: str
    nacionalidad: str


userList = [
    Director(id=1, dni="12345678A", name="John", apellidos="Doe", nacionalidad="USA"),
    Director(id=2, dni="87654321B", name="Jane", apellidos="Smith", nacionalidad="UK"),
    Director(
        id=3, dni="11223344C", name="Alice", apellidos="Johnson", nacionalidad="Canada"
    ),
    Director(
        id=4, dni="44332211D", name="Bob", apellidos="Brown", nacionalidad="Australia"
    ),
    Director(
        id=5,
        dni="55667788E",
        name="Charlie",
        apellidos="Davis",
        nacionalidad="New Zealand",
    ),
    Director(
        id=6, dni="99887766F", name="Eve", apellidos="Wilson", nacionalidad="Ireland"
    ),
    Director(
        id=7, dni="66778899G", name="Frank", apellidos="Garcia", nacionalidad="Spain"
    ),
    Director(
        id=8, dni="33445566H", name="Grace", apellidos="Martinez", nacionalidad="Mexico"
    ),
    Director(
        id=9,
        dni="22113344I",
        name="Hank",
        apellidos="Rodriguez",
        nacionalidad="Argentina",
    ),
    Director(
        id=10, dni="44556677J", name="Ivy", apellidos="Lopez", nacionalidad="Colombia"
    ),
]

app = FastAPI()


@app.get("/users")
def root():
    return userList


@app.get("/users/{user_id}")
def userById(user_id: int):
    users = [user for user in userList if user.id == user_id]

    if len(users) != 0:
        return users[0]
    else:
        return {"error": "User not found"}
