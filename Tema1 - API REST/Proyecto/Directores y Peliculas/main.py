from routers import directores, peliculas,auth_users
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.include_router(directores.router)
app.include_router(peliculas.router)
app.include_router(auth_users.router)
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def inicio():
    return {"Hello" : "World"}