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