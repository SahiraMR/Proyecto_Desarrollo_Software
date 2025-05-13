from pydantic import BaseModel
from typing import Optional
from datetime import date

class Comentario(BaseModel):
    id: Optional[int] = None
    libro_id: int
    usuario: str
    contenido: str
    fecha: date
