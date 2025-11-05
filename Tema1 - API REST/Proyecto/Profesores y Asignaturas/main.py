from fastapi import FastAPI
from routers import asignaturas,profesores


app = FastAPI()

app.include_router(asignaturas.router)
app.include_router(profesores.router)