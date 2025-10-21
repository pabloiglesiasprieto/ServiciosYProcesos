from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Director(BaseModel):
    id: int
    dni: str
    nombre: str
    apellidos: str
    nacionalidad: str
    

listaDirectores = [
    {"id": 1, "dni": "12345678A", "nombre": "Steven", "apellidos": "Spielberg", "nacionalidad": "Estadounidense"},
    {"id": 2, "dni": "23456789B", "nombre": "Martin", "apellidos": "Scorsese", "nacionalidad": "Estadounidense"},
    {"id": 3, "dni": "34567890C", "nombre": "Christopher", "apellidos": "Nolan", "nacionalidad": "Británico"},
    {"id": 4, "dni": "45678901D", "nombre": "Quentin", "apellidos": "Tarantino", "nacionalidad": "Estadounidense"},
    {"id": 5, "dni": "56789012E", "nombre": "Pedro", "apellidos": "Almodóvar", "nacionalidad": "Español"},
    {"id": 6, "dni": "67890123F", "nombre": "Guillermo", "apellidos": "del Toro", "nacionalidad": "Mexicano"},
    {"id": 7, "dni": "78901234G", "nombre": "Sofia", "apellidos": "Coppola", "nacionalidad": "Estadounidense"},
    {"id": 8, "dni": "89012345H", "nombre": "Alejandro", "apellidos": "González Iñárritu", "nacionalidad": "Mexicano"},
    {"id": 9, "dni": "90123456I", "nombre": "Greta", "apellidos": "Gerwig", "nacionalidad": "Estadounidense"},
    {"id": 10, "dni": "01234567J", "nombre": "Denis", "apellidos": "Villeneuve", "nacionalidad": "Canadiense"},
    {"id": 11, "dni": "12345678K", "nombre": "Bong", "apellidos": "Joon-ho", "nacionalidad": "Surcoreano"},
    {"id": 12, "dni": "23456789L", "nombre": "Wes", "apellidos": "Anderson", "nacionalidad": "Estadounidense"},
    {"id": 13, "dni": "34567890M", "nombre": "Kathryn", "apellidos": "Bigelow", "nacionalidad": "Estadounidense"},
    {"id": 14, "dni": "45678901N", "nombre": "Alfonso", "apellidos": "Cuarón", "nacionalidad": "Mexicano"},
    {"id": 15, "dni": "56789012O", "nombre": "Ava", "apellidos": "DuVernay", "nacionalidad": "Estadounidense"},
    {"id": 16, "dni": "67890123P", "nombre": "David", "apellidos": "Fincher", "nacionalidad": "Estadounidense"},
    {"id": 17, "dni": "78901234Q", "nombre": "Paolo", "apellidos": "Sorrentino", "nacionalidad": "Italiano"},
    {"id": 18, "dni": "89012345R", "nombre": "Jane", "apellidos": "Campion", "nacionalidad": "Neozelandesa"},
    {"id": 19, "dni": "90123456S", "nombre": "Park", "apellidos": "Chan-wook", "nacionalidad": "Surcoreano"},
    {"id": 20, "dni": "01234567T", "nombre": "Ridley", "apellidos": "Scott", "nacionalidad": "Británico"}
]


@app.get("/directores")
def get_directores():
    return listaDirectores

@app.get("/directores/{director_id}")
def get_director(director_id: int):
    lista = [director for director in listaDirectores if director["id"] == director_id]
    return lista[0] if lista else {"error": "Director no encontrado"}

@app.get("/directores/nacionalidad/{nacionalidad}")
def get_directores_por_nacionalidad(nacionalidad: str):
    lista = [director for director in listaDirectores if director["nacionalidad"].lower() == nacionalidad.lower()]
    return lista if lista else {"error": "No se encontraron directores con esa nacionalidad"}

@app.get("/directores/nombre/{empieza_con}")
def get_directores_por_nombre(empieza_con: str):
    lista = [director for director in listaDirectores if director["nombre"].lower().startswith(empieza_con.lower())]
    return lista if lista else {"error": "No se encontraron directores que empiecen por {empieza_con}"}

@app.get("/directores/dni/{dni}")
def get_director_por_dni(dni: str):
    lista = [director for director in listaDirectores if director["dni"].lower() == dni.lower()]
    return lista[0] if lista else {"error": "Director no encontrado con ese DNI"}

@app.get("/directores/apellidos/{apellidos}")
def get_directores_por_apellidos(apellidos: str):
    lista = [director for director in listaDirectores if director["apellidos"].lower() == apellidos.lower()]
    return lista[0] if lista else {"error": "No se encontraron directores con esos apellidos"}