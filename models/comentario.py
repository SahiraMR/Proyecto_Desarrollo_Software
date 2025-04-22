from pydantic import BaseModel

class Comentario(BaseModel):
    id: int = None
    libro_id: int
    texto: str
