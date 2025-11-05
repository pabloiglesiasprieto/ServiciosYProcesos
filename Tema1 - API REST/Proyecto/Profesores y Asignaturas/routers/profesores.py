from fastapi import APIRouter
from pydantic import BaseModel


class Profesor(BaseModel):
    id: int
    dni: str
    nombre: str
    apellido: str
    telefono : str
    direccion : str
    cuentaBancaria : str
    
router = APIRouter(prefix="/profesores")