

from pydantic import BaseModel

class Comentario(BaseModel):
    id: int
    libro_id: int
    contenido: str
    autor: str
    calificacion: int  # de 1 a 5
