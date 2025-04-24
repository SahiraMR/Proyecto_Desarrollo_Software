from pydantic import BaseModel 

class Autor(BaseModel):
    id: int
    nombre: str

h