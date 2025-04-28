from pydantic import BaseModel




class Autor(BaseModel):
    id: int = None
    nombre: str
    nombre_libro: str
    genero: str  
