from fastapi import APIRouter, FastAPI, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/directores", tags=["directores"])

class Director(BaseModel):
    id: int
    dni: str
    nombre: str
    apellidos: str
    nacionalidad: str


listaDirectores = [
    Director(id=1, dni="12345678A", nombre="Steven", apellidos="Spielberg", nacionalidad="Estadounidense"),
    Director(id=2, dni="23456789B", nombre="Martin", apellidos="Scorsese", nacionalidad="Estadounidense"),
    Director(id=3, dni="34567890C", nombre="Christopher", apellidos="Nolan", nacionalidad="Británico"),
    Director(id=4, dni="45678901D", nombre="Quentin", apellidos="Tarantino", nacionalidad="Estadounidense"),
    Director(id=5, dni="56789012E", nombre="Pedro", apellidos="Almodóvar", nacionalidad="Español"),
    Director(id=6, dni="67890123F", nombre="Guillermo", apellidos="del Toro", nacionalidad="Mexicano"),
    Director(id=7, dni="78901234G", nombre="Sofia", apellidos="Coppola", nacionalidad="Estadounidense"),
    Director(id=8, dni="89012345H", nombre="Alejandro", apellidos="González Iñárritu", nacionalidad="Mexicano"),
    Director(id=9, dni="90123456I", nombre="Greta", apellidos="Gerwig", nacionalidad="Estadounidense"),
    Director(id=10, dni="01234567J", nombre="Denis", apellidos="Villeneuve", nacionalidad="Canadiense"),
    Director(id=11, dni="12345678K", nombre="Bong", apellidos="Joon-ho", nacionalidad="Surcoreano"),
    Director(id=12, dni="23456789L", nombre="Wes", apellidos="Anderson", nacionalidad="Estadounidense"),
    Director(id=13, dni="34567890M", nombre="Kathryn", apellidos="Bigelow", nacionalidad="Estadounidense"),
    Director(id=14, dni="45678901N", nombre="Alfonso", apellidos="Cuarón", nacionalidad="Mexicano"),
    Director(id=15, dni="56789012O", nombre="Ava", apellidos="DuVernay", nacionalidad="Estadounidense"),
    Director(id=16, dni="67890123P", nombre="David", apellidos="Fincher", nacionalidad="Estadounidense"),
    Director(id=17, dni="78901234Q", nombre="Paolo", apellidos="Sorrentino", nacionalidad="Italiano"),
    Director(id=18, dni="89012345R", nombre="Jane", apellidos="Campion", nacionalidad="Neozelandesa"),
    Director(id=19, dni="90123456S", nombre="Park", apellidos="Chan-wook", nacionalidad="Surcoreano"),
    Director(id=20, dni="01234567T", nombre="Ridley", apellidos="Scott", nacionalidad="Británico"),
]


# region utils
def findById(director_id):
    lista = [director for director in listaDirectores if director.id == director_id]
    if lista:
        return lista[0]
    raise HTTPException(status_code=404, detail="Director no encontrado")

def lastID():
    if listaDirectores:
        return max(listaDirectores, key=id).id+1
    return 0
#endregion utils

# region gets
@router.get("/")
def get_directores():
    return listaDirectores


@router.get("")
def get_directores(id: int):
    return findById(id)


@router.get("/{director_id}")
def get_director(director_id: int):
    return findById(director_id)


@router.get("/nacionalidad/{nacionalidad}")
def get_directores_por_nacionalidad(nacionalidad: str):
    lista = [
        director
        for director in listaDirectores
        if director.nacionalidad.lower() == nacionalidad.lower()
    ]

    if lista:
        return lista[0]
    else:
        raise HTTPException(status_code=404, detail="Director no encontrado")


@router.get("/nombre/{empieza_con}")
def get_directores_por_nombre(empieza_con: str):
    lista = [
        director
        for director in listaDirectores
        if director.nombre.lower().startswith(empieza_con.lower())
    ]
    if lista:
        return lista[0]
    else:
        raise HTTPException(status_code=404, detail="Director no encontrado")


@router.get("/dni/{dni}")
def get_director_por_dni(dni: str):
    lista = [
        director
        for director in listaDirectores
        if director["dni"].lower() == dni.lower()
    ]
    if lista:
        return lista[0]
    else:
        raise HTTPException(status_code=404, detail="Director no encontrado")


@router.get("/apellidos/{apellidos}")
def get_directores_por_apellidos(apellidos: str):
    lista = [
        director
        for director in listaDirectores
        if director.apellidos.lower() == apellidos.lower()
    ]
    if lista:
        return lista[0]
    else:
        raise HTTPException(status_code=404, detail="Director no encontrado")
    
#endregion gets
#region posts
@router.post("/", response_model=Director, status_code=201)
def crear_director(director: Director):
    director.id = lastID()
    listaDirectores.append(director)
    return director
#endregion posts
#region puts
@router.put("/{director_id}", response_model=Director)
def actualizar_director(director_id: int, director_actualizado: Director):
    for index, director in enumerate(listaDirectores):
        if director.id == director_id:
            director_actualizado.id = director_id
            listaDirectores[index] = director_actualizado
            return listaDirectores[index]
    raise HTTPException(status_code=404, detail="Director no encontrado")
#endregion puts
#region deletes
@router.delete("/{director_id}")
def eliminar_director(director_id: int):
    for director in listaDirectores:
        if director.id == director_id:
            listaDirectores.remove(director)
            return {}
    raise HTTPException(status_code=404, detail="Director no encontrado")
#endregion deletes