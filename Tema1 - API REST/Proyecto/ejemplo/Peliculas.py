from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Pelicula(BaseModel):
    id: int
    titulo: str
    duracion: int # minutos
    idDirector: int # FK de Director.id

listaPeliculas = [
Pelicula(id=1, titulo="Inception", duracion=148, idDirector=3),
Pelicula(id=2, titulo="Pulp Fiction", duracion=154, idDirector=4),
Pelicula(id=3, titulo="Amores Perros", duracion=154, idDirector=8),
Pelicula(id=4, titulo="Parásitos", duracion=132, idDirector=11),
Pelicula(id=5, titulo="La forma del agua", duracion=123, idDirector=6),
Pelicula(id=6, titulo="Los abrazos rotos", duracion=127, idDirector=5),
Pelicula(id=7, titulo="Tenet", duracion=150, idDirector=3),
Pelicula(id=8, titulo="El irlandés", duracion=209, idDirector=2),
Pelicula(id=9, titulo="Barbie", duracion=114, idDirector=9),
Pelicula(id=10, titulo="Dune", duracion=155, idDirector=10),
Pelicula(id=11, titulo="Jurassic Park", duracion=127, idDirector=1),
Pelicula(id=12, titulo="Schindler's List", duracion=195, idDirector=1),
Pelicula(id=13, titulo="Taxi Driver", duracion=114, idDirector=2),
Pelicula(id=14, titulo="El caballero oscuro", duracion=152, idDirector=3),
Pelicula(id=15, titulo="Kill Bill Vol.1", duracion=111, idDirector=4),
Pelicula(id=16, titulo="Kill Bill Vol.2", duracion=136, idDirector=4),
Pelicula(id=17, titulo="Dolor y gloria", duracion=113, idDirector=5),
Pelicula(id=18, titulo="El laberinto del fauno", duracion=118, idDirector=6),
Pelicula(id=19, titulo="Lost in Translation", duracion=102, idDirector=7),
Pelicula(id=20, titulo="Babel", duracion=143, idDirector=8),
Pelicula(id=21, titulo="Little Women", duracion=135, idDirector=9),
Pelicula(id=22, titulo="Blade Runner 2049", duracion=163, idDirector=10),
Pelicula(id=23, titulo="Memories of Murder", duracion=132, idDirector=11),
Pelicula(id=24, titulo="The Grand Budapest Hotel", duracion=99, idDirector=12),
Pelicula(id=25, titulo="Zero Dark Thirty", duracion=157, idDirector=13),
Pelicula(id=26, titulo="Roma", duracion=135, idDirector=14),
Pelicula(id=27, titulo="Selma", duracion=128, idDirector=15),
Pelicula(id=28, titulo="Fight Club", duracion=139, idDirector=16),
Pelicula(id=29, titulo="The Social Network", duracion=120, idDirector=16),
Pelicula(id=30, titulo="La grande bellezza", duracion=141, idDirector=17),
Pelicula(id=31, titulo="The Power of the Dog", duracion=126, idDirector=18),
Pelicula(id=32, titulo="Oldboy", duracion=120, idDirector=19),
Pelicula(id=33, titulo="The Last Duel", duracion=152, idDirector=20),
Pelicula(id=34, titulo="Alien", duracion=117, idDirector=20),
Pelicula(id=35, titulo="Sicario", duracion=121, idDirector=10),
Pelicula(id=36, titulo="Prisoners", duracion=153, idDirector=10),
Pelicula(id=37, titulo="Seven", duracion=127, idDirector=16),
Pelicula(id=38, titulo="Mank", duracion=131, idDirector=16),
Pelicula(id=39, titulo="Her", duracion=126, idDirector=12),
Pelicula(id=40, titulo="The Shape of Water", duracion=123, idDirector=6),
]

#region utils

def findById(pelicula_id):
    lista = [p for p in listaPeliculas if p.id == pelicula_id]
    if lista:
        return lista[0]
    raise HTTPException(status_code=404, detail="Película no encontrada")

def lastID():
    if listaPeliculas:
        return max(listaPeliculas, key=id).id + 1

#endregion utils
#region gets

@app.get("/peliculas")
def get_peliculas():
    return listaPeliculas

@app.get("/peliculas/{pelicula_id}")
def get_pelicula(pelicula_id: int):
    return findById(pelicula_id)

@app.get("/peliculas/director/{idDirector}")
def get_peliculas_por_director(idDirector: int):
    lista = [p for p in listaPeliculas if p.idDirector == idDirector]
    if lista:
        return lista
    raise HTTPException(status_code=404, detail="No hay películas para ese director")

@app.get("/peliculas/titulo/{empieza_con}")
def get_peliculas_por_titulo(empieza_con: str):
    lista = [p for p in listaPeliculas if p.titulo.lower().startswith(empieza_con.lower())]
    if lista:
        return lista
    raise HTTPException(status_code=404, detail="Película no encontrada")

#endregion gets
#region posts

@app.post("/peliculas", response_model=Pelicula, status_code=201)
def crear_pelicula(pelicula: Pelicula):
    pelicula.id = lastID()
    listaPeliculas.append(pelicula)
    return pelicula

#endregion posts
#region puts

@app.put("/peliculas/{pelicula_id}", response_model=Pelicula)
def actualizar_pelicula(pelicula_id: int, pelicula_actualizada: Pelicula):
    for index, p in enumerate(listaPeliculas):
        if p.id == pelicula_id:
            pelicula_actualizada.id = pelicula_id
            listaPeliculas[index] = pelicula_actualizada
            return listaPeliculas[index]
    raise HTTPException(status_code=404, detail="Película no encontrada")

#endregion puts
#region deletes

@app.delete("/peliculas/{pelicula_id}")
def eliminar_pelicula(pelicula_id: int):
    for p in listaPeliculas:
        if p.id == pelicula_id:
            listaPeliculas.remove(p)
        return {}
    raise HTTPException(status_code=404, detail="Película no encontrada")

#endregion deletes