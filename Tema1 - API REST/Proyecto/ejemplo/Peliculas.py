from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI()


class Pelicula(BaseModel):
    id: int
    ISBN: str
    Titulo: str
    duracion: str
    idDirector: int


listaPelicula: list[Pelicula] = [
    Pelicula(
        id=1,
        ISBN="0-13-041717-3",
        Titulo="Como ser un femboy",
        duracion="∞",
        idDirector=1,
    ),
    Pelicula(
        id=2,
        ISBN="0-13-041718-1",
        Titulo="El hacker del amor",
        duracion="120",
        idDirector=7,
    ),
    Pelicula(
        id=3,
        ISBN="0-13-041719-0",
        Titulo="Los gatos del apocalipsis",
        duracion="95",
        idDirector=14,
    ),
    Pelicula(
        id=4,
        ISBN="0-13-041720-9",
        Titulo="Sueños de neón",
        duracion="110",
        idDirector=2,
    ),
    Pelicula(
        id=5,
        ISBN="0-13-041721-7",
        Titulo="El código del destino",
        duracion="132",
        idDirector=11,
    ),
    Pelicula(
        id=6,
        ISBN="0-13-041722-5",
        Titulo="La venganza del tostador",
        duracion="88",
        idDirector=9,
    ),
    Pelicula(
        id=7,
        ISBN="0-13-041723-3",
        Titulo="Piratas del sistema",
        duracion="143",
        idDirector=4,
    ),
    Pelicula(
        id=8,
        ISBN="0-13-041724-1",
        Titulo="El último bug",
        duracion="117",
        idDirector=19,
    ),
    Pelicula(
        id=9,
        ISBN="0-13-041725-X",
        Titulo="Corazones binarios",
        duracion="105",
        idDirector=16,
    ),
    Pelicula(
        id=10,
        ISBN="0-13-041726-8",
        Titulo="404: Amor no encontrado",
        duracion="98",
        idDirector=12,
    ),
    Pelicula(
        id=11,
        ISBN="0-13-041727-6",
        Titulo="El algoritmo del miedo",
        duracion="125",
        idDirector=3,
    ),
    Pelicula(
        id=12,
        ISBN="0-13-041728-4",
        Titulo="La rebelión de los NPCs",
        duracion="111",
        idDirector=17,
    ),
    Pelicula(
        id=13, ISBN="0-13-041729-2", Titulo="Pixel Noir", duracion="107", idDirector=5
    ),
    Pelicula(
        id=14,
        ISBN="0-13-041730-6",
        Titulo="La torre del wifi",
        duracion="113",
        idDirector=10,
    ),
    Pelicula(
        id=15, ISBN="0-13-041731-4", Titulo="Romance.exe", duracion="99", idDirector=18
    ),
    Pelicula(
        id=16,
        ISBN="0-13-041732-2",
        Titulo="El router perdido",
        duracion="102",
        idDirector=6,
    ),
    Pelicula(
        id=17,
        ISBN="0-13-041733-0",
        Titulo="Silicio en la niebla",
        duracion="115",
        idDirector=2,
    ),
    Pelicula(
        id=18,
        ISBN="0-13-041734-9",
        Titulo="Amor en modo oscuro",
        duracion="121",
        idDirector=13,
    ),
    Pelicula(
        id=19,
        ISBN="0-13-041735-7",
        Titulo="La señal del más allá",
        duracion="97",
        idDirector=1,
    ),
    Pelicula(
        id=20,
        ISBN="0-13-041736-5",
        Titulo="Quantum Lovers",
        duracion="134",
        idDirector=20,
    ),
    Pelicula(
        id=21,
        ISBN="0-13-041737-3",
        Titulo="El dragón de silicio",
        duracion="119",
        idDirector=8,
    ),
    Pelicula(
        id=22,
        ISBN="0-13-041738-1",
        Titulo="Sueños en alta definición",
        duracion="101",
        idDirector=3,
    ),
    Pelicula(
        id=23, ISBN="0-13-041739-X", Titulo="Neural Hearts", duracion="96", idDirector=9
    ),
    Pelicula(
        id=24,
        ISBN="0-13-041740-8",
        Titulo="Bajo el mismo firewall",
        duracion="124",
        idDirector=14,
    ),
    Pelicula(
        id=25,
        ISBN="0-13-041741-6",
        Titulo="El servidor fantasma",
        duracion="108",
        idDirector=5,
    ),
    Pelicula(
        id=26,
        ISBN="0-13-041742-4",
        Titulo="La sombra del algoritmo",
        duracion="130",
        idDirector=17,
    ),
    Pelicula(
        id=27,
        ISBN="0-13-041743-2",
        Titulo="Las crónicas del metaverso",
        duracion="140",
        idDirector=19,
    ),
    Pelicula(
        id=28,
        ISBN="0-13-041744-0",
        Titulo="Byte a mi corazón",
        duracion="103",
        idDirector=10,
    ),
    Pelicula(
        id=29,
        ISBN="0-13-041745-9",
        Titulo="Error Fatal 404",
        duracion="100",
        idDirector=7,
    ),
    Pelicula(
        id=30,
        ISBN="0-13-041746-7",
        Titulo="Los androides también sueñan",
        duracion="118",
        idDirector=12,
    ),
    Pelicula(
        id=31,
        ISBN="0-13-041747-5",
        Titulo="Amor en la nube",
        duracion="99",
        idDirector=16,
    ),
    Pelicula(
        id=32,
        ISBN="0-13-041748-3",
        Titulo="El apagón digital",
        duracion="106",
        idDirector=4,
    ),
    Pelicula(
        id=33,
        ISBN="0-13-041749-1",
        Titulo="Los guardianes del wifi",
        duracion="94",
        idDirector=18,
    ),
    Pelicula(
        id=34,
        ISBN="0-13-041750-5",
        Titulo="Encriptado para siempre",
        duracion="127",
        idDirector=6,
    ),
    Pelicula(
        id=35,
        ISBN="0-13-041751-3",
        Titulo="404: Pasión no encontrada",
        duracion="112",
        idDirector=15,
    ),
    Pelicula(
        id=36,
        ISBN="0-13-041752-1",
        Titulo="Debugging my feelings",
        duracion="109",
        idDirector=8,
    ),
    Pelicula(
        id=37,
        ISBN="0-13-041753-X",
        Titulo="Cyberpunk Dreams",
        duracion="137",
        idDirector=20,
    ),
    Pelicula(
        id=38,
        ISBN="0-13-041754-8",
        Titulo="La conexión perdida",
        duracion="116",
        idDirector=2,
    ),
    Pelicula(
        id=39,
        ISBN="0-13-041755-6",
        Titulo="Servidor caído",
        duracion="123",
        idDirector=11,
    ),
    Pelicula(
        id=40,
        ISBN="0-13-041756-4",
        Titulo="El amor en tiempos de IA",
        duracion="126",
        idDirector=9,
    ),
]


# region get
@app.get("/peliculas")
def getPeliculas():
    return listaPelicula


@app.get("/peliculas/{id_pelicula}")
def getPeliculaByID(id_pelicula: int):
    lista = [pelicula for pelicula in listaPelicula if pelicula.id == id_pelicula]
    if lista:
        return lista[0]
    raise HTTPException(status_code=404, detail="No hay pelicula.")


# endregion get
