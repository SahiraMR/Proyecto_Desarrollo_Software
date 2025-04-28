from fastapi import FastAPI, HTTPException
from crud import libros_crud, autores_crud, comentarios_crud

app = FastAPI()

# Libros
@app.get("/libros")
def listar_libros():
    return libros_crud.listar_libros()

@app.post("/libros")
def crear_libro(libro: libros_crud.Libro):
    return libros_crud.crear_libro(libro)

@app.put("/libros/{id}")
def actualizar_libro(id: int, libro: libros_crud.Libro):
    return libros_crud.actualizar_libro(id, libro)

@app.delete("/libros/{id}")
def eliminar_libro(id: int):
    return libros_crud.eliminar_libro(id)

@app.get("/libros/filtrar-genero")
def filtrar_por_genero(genero: str):
    return libros_crud.filtrar_por_genero(genero)

@app.get("/libros/buscar")
def buscar_por_nombre(nombre: str):
    return libros_crud.buscar_por_nombre(nombre)

# Autores
@app.get("/autores")
def listar_autores():
    return autores_crud.listar_autores()

@app.post("/autores")
def crear_autor(autor: autores_crud.Autor):
    return autores_crud.crear_autor(autor)

@app.put("/autores/{id}")
def actualizar_autor(id: int, autor: autores_crud.Autor):
    return autores_crud.actualizar_autor(id, autor)

@app.delete("/autores/{id}")
def eliminar_autor(id: int):
    return autores_crud.eliminar_autor(id)

# Comentarios
@app.get("/comentarios")
def listar_comentarios():
    return comentarios_crud.listar_comentarios()

@app.post("/comentarios")
def agregar_comentario(comentario: comentarios_crud.Comentario):
    return comentarios_crud.agregar_comentario(comentario)

@app.put("/comentarios/{id}")
def actualizar_comentario(id: int, comentario: comentarios_crud.Comentario):
    return comentarios_crud.actualizar_comentario(id, comentario)

@app.delete("/comentarios/{id}")
def eliminar_comentario(id: int):
    return comentarios_crud.eliminar_comentario(id)
