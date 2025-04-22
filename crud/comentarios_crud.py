import csv
from pathlib import Path
from models.comentario import Comentario
from typing import List

DATA_PATH = Path("data/comentarios.csv")

def agregar_comentario(comentario: Comentario):
    comentario.id = obtener_nuevo_id()
    with open(DATA_PATH, 'a', newline='', encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "libro_id", "texto"])
        if DATA_PATH.stat().st_size == 0:
            writer.writeheader()
        writer.writerow(comentario.dict())
    return comentario

def obtener_nuevo_id():
    if not DATA_PATH.exists() or DATA_PATH.stat().st_size == 0:
        return 1
    with open(DATA_PATH, newline='', encoding="utf-8") as f:
        reader = csv.DictReader(f)
        ids = [int(row["id"]) for row in reader]
        return max(ids, default=0) + 1

def listar_comentarios():
    if not DATA_PATH.exists():
        return []
    with open(DATA_PATH, newline='', encoding="utf-8") as f:
        return list(csv.DictReader(f))
