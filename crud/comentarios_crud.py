import csv
import os
from fastapi import HTTPException
from models.comentario import Comentario
from typing import List
from pathlib import Path

# Rutas de archivos
DATA_PATH = Path("data/comentarios.csv")
ELIMINADOS_PATH = Path("data/comentarios_eliminados.csv")


def leer_csv() -> List[dict]:
    if not DATA_PATH.exists():
        return []
    with open(DATA_PATH, newline='', encoding="utf-8") as f:
        return list(csv.DictReader(f))



def escribir_csv(comentarios: List[dict]):
    with open(DATA_PATH, 'w', newline='', encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "nombre", "calificacion"])
        writer.writeheader()
        writer.writerows(comentarios)

def listar_comentarios():
    return leer_csv()

def agregar_comentario(comentario: Comentario):
    comentarios = leer_csv()
    if not (1 <= comentario.calificacion <= 5):
        raise HTTPException(status_code=400, detail="La calificación debe estar entre 1 y 5.")
    comentario.id = max([int(c["id"]) for c in comentarios], default=0) + 1
    comentarios.append(comentario.dict())
    escribir_csv(comentarios)
    return comentario

def actualizar_comentario(id: int, comentario: Comentario):
    comentarios = leer_csv()
    for i, c in enumerate(comentarios):
        if int(c["id"]) == id:
            if not (1 <= comentario.calificacion <= 5):
                raise HTTPException(status_code=400, detail="La calificación debe estar entre 1 y 5.")
            comentarios[i] = comentario.dict()
            comentarios[i]["id"] = str(id)
            escribir_csv(comentarios)
            return comentario
    raise HTTPException(status_code=404, detail="Comentario no encontrado")

def eliminar_comentario(id: int):
    comentarios = leer_csv()
    comentario_encontrado = None
    nuevos_comentarios = []
    for c in comentarios:
        if int(c["id"]) == id:
            comentario_encontrado = c
        else:
            nuevos_comentarios.append(c)

    if not comentario_encontrado:
        raise HTTPException(status_code=404, detail="Comentario no encontrado")

    escribir_csv(nuevos_comentarios)
    with open(ELIMINADOS_PATH, 'a', newline='', encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=comentario_encontrado.keys())
        if os.stat(ELIMINADOS_PATH).st_size == 0:
            writer.writeheader()
        writer.writerow(comentario_encontrado)
    return {"mensaje": "Comentario eliminado y registrado en historial."}
