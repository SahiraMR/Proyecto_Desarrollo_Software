from pydantic import BaseModel
class Libro(BaseModel):
   id: int = None
   titulo: str
   autor_id: int
   anio_publicacion: int
   genero: str
   plataforma: str