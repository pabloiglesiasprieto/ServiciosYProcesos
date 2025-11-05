from fastapi import APIRouter, HTTPException
from pydantic import BaseModel


class Asignatura(BaseModel):
    id: int
    titulo: str
    numHoras: int
    idProfesor: int


router = APIRouter(prefix="/asignaturas")

listaAsignatura = [
    Asignatura(id=1, titulo="Programación I", numHoras=20, idProfesor=1),
    Asignatura(id=2, titulo="Programación II", numHoras=25, idProfesor=2),
    Asignatura(id=3, titulo="Bases de Datos I", numHoras=30, idProfesor=3),
    Asignatura(id=4, titulo="Bases de Datos II", numHoras=30, idProfesor=4),
    Asignatura(id=5, titulo="Sistemas Operativos", numHoras=40, idProfesor=5),
    Asignatura(id=6, titulo="Redes de Computadores", numHoras=35, idProfesor=6),
    Asignatura(id=7, titulo="Ingeniería del Software", numHoras=25, idProfesor=7),
    Asignatura(id=8, titulo="Análisis de Algoritmos", numHoras=30, idProfesor=8),
    Asignatura(id=9, titulo="Estructuras de Datos", numHoras=30, idProfesor=9),
    Asignatura(id=10, titulo="Matemáticas Discretas", numHoras=25, idProfesor=10),
    Asignatura(id=11, titulo="Álgebra Lineal", numHoras=30, idProfesor=11),
    Asignatura(id=12, titulo="Cálculo", numHoras=35, idProfesor=12),
    Asignatura(id=13, titulo="Inteligencia Artificial", numHoras=40, idProfesor=13),
    Asignatura(id=14, titulo="Machine Learning", numHoras=40, idProfesor=14),
    Asignatura(id=15, titulo="Deep Learning", numHoras=35, idProfesor=15),
    Asignatura(id=16, titulo="Computación Gráfica", numHoras=25, idProfesor=16),
    Asignatura(
        id=17, titulo="Arquitectura de Computadores", numHoras=30, idProfesor=17
    ),
    Asignatura(id=18, titulo="Seguridad Informática", numHoras=35, idProfesor=18),
    Asignatura(id=19, titulo="Criptografía", numHoras=30, idProfesor=19),
    Asignatura(id=20, titulo="Gestión de Proyectos", numHoras=25, idProfesor=20),
    Asignatura(id=21, titulo="Programación Web I", numHoras=30, idProfesor=1),
    Asignatura(id=22, titulo="Programación Web II", numHoras=30, idProfesor=2),
    Asignatura(id=23, titulo="Desarrollo Móvil", numHoras=35, idProfesor=3),
    Asignatura(id=24, titulo="Desarrollo de Videojuegos", numHoras=40, idProfesor=4),
    Asignatura(id=25, titulo="Computación en la Nube", numHoras=30, idProfesor=5),
    Asignatura(id=26, titulo="Big Data", numHoras=35, idProfesor=6),
    Asignatura(id=27, titulo="Internet de las Cosas", numHoras=25, idProfesor=7),
    Asignatura(id=28, titulo="Robótica", numHoras=30, idProfesor=8),
    Asignatura(id=29, titulo="Ética Profesional", numHoras=20, idProfesor=9),
    Asignatura(id=30, titulo="Metodologías Ágiles", numHoras=25, idProfesor=10),
    Asignatura(id=31, titulo="Testing de Software", numHoras=30, idProfesor=11),
    Asignatura(
        id=32, titulo="Administración de Servidores", numHoras=35, idProfesor=12
    ),
    Asignatura(id=33, titulo="Sistemas Distribuidos", numHoras=40, idProfesor=13),
    Asignatura(id=34, titulo="Computación Paralela", numHoras=30, idProfesor=14),
    Asignatura(id=35, titulo="Ciberseguridad Avanzada", numHoras=35, idProfesor=15),
    Asignatura(id=36, titulo="Blockchain", numHoras=25, idProfesor=16),
    Asignatura(id=37, titulo="Realidad Virtual", numHoras=30, idProfesor=17),
    Asignatura(id=38, titulo="Realidad Aumentada", numHoras=30, idProfesor=18),
    Asignatura(id=39, titulo="DevOps", numHoras=25, idProfesor=19),
    Asignatura(
        id=40, titulo="Administración de Bases de Datos", numHoras=35, idProfesor=20
    )
]
#region utils
def buscarUltimaID():
    return max(listaAsignatura, key=id).id +1
#endregion utils

#region get
@router.get("/")
def getAsignatura():
    return listaAsignatura

@router.get("/{asignatura_id}")
def getAsignaturaPorID(asignatura_id : int):
    pelicula = [asignatura for asignatura in listaAsignatura if asignatura.id == asignatura_id]
    if pelicula:
        return pelicula [0]
    raise HTTPException (status_code=404, detail="Asignatura no encontrada")

@router.get("/profesor_id/{profesor_id}")
def getAsignaturaPorProfesorID(profesor_id:int):
    pelicula = [asignatura for asignatura in listaAsignatura if asignatura.idProfesor == profesor_id]
    if pelicula:
        return pelicula [0]
    raise HTTPException (status_code=404, detail="Asignatura no encontrada")
#endregion get
    
#region post
@router.post("/", response_model=Asignatura, status_code=201)
def insertarAsignatura(Asignatura : Asignatura):
    Asignatura.id = buscarUltimaID()
    listaAsignatura.append(Asignatura)
    return Asignatura
#endregion post
#region 