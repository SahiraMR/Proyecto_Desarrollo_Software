from pydantic import BaseModel

class Comentario(BaseModel):
    id: int = None
    nombre: str
    calificacion: int
