import csv
import os
from fastapi import HTTPException
from models.autor import Autor
from typing import List
from pathlib import Path

# Rutas de archivos
DATA_PATH = Path("data/autores.csv")
ELIMINADOS_PATH = Path("data/autores_eliminados.csv")

def leer_csv() -> List[dict]:
    if not DATA_PATH.exists():
        return []
    with open(DATA_PATH, newline='', encoding="utf-8") as f:
        return list(csv.DictReader(f))
    

def escribir_csv(autores: List[dict]):
    with open(DATA_PATH, 'w', newline='', encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "nombre", "nombre_libro", "genero"])
        writer.writeheader()
        writer.writerows(autores)

def listar_autores():
    return leer_csv()

def crear_autor(autor: Autor):
    autores = leer_csv()
    autor.id = max([int(a["id"]) for a in autores], default=0) + 1
    autor_dict = autor.dict()
    print(f"Autor creado: {autor_dict}")  # Para ver el contenido antes de agregarlo
    autores.append(autor_dict)
    escribir_csv(autores)
    return autor

def actualizar_autor(id: int, autor: Autor):
    autores = leer_csv()
    for i, a in enumerate(autores):
        if int(a["id"]) == id:
            autores[i] = autor.dict()
            autores[i]["id"] = str(id)
            escribir_csv(autores)
            return autor
    raise HTTPException(status_code=404, detail="Autor no encontrado")

def eliminar_autor(id: int):
    autores = leer_csv()
    autor_encontrado = None
    nuevos_autores = []
    for a in autores:
        if int(a["id"]) == id:
            autor_encontrado = a
        else:
            nuevos_autores.append(a)

    if not autor_encontrado:
        raise HTTPException(status_code=404, detail="Autor no encontrado")