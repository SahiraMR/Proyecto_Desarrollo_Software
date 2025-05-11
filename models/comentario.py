from pydantic import BaseModel

class Comentario(BaseModel):
    id: int = None  # se asigna automáticamente
    usuario: str
    contenido: str
    fecha: str  # formato YYYY-MM-DD
