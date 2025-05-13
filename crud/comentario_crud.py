import csv
import os
from fastapi import HTTPException
from typing import List
from pathlib import Path
from models.comentario import Comentario  # Asegúrate de que tenga 'libro_id'
from datetime import date

DATA_PATH = Path("data/comentarios.csv")
ELIMINADOS_PATH = Path("data/comentarios_eliminados.csv")

# Crear carpeta si no existe
DATA_PATH.parent.mkdir(parents=True, exist_ok=True)

def leer_csv() -> List[dict]:
    if not DATA_PATH.exists():
        return []
    with open(DATA_PATH, newline='', encoding="utf-8") as f:
        return list(csv.DictReader(f))

def escribir_csv(comentarios: List[dict]):
    with open(DATA_PATH, 'w', newline='', encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "libro_id", "usuario", "contenido", "fecha"])
        writer.writeheader()
        writer.writerows(comentarios)

def listar_comentarios():
    return leer_csv()

def crear_comentario(comentario: Comentario):
    comentarios = leer_csv()
    comentario.id = max([int(c["id"]) for c in comentarios], default=0) + 1
    comentario_dict = comentario.dict()

    comentario_dict["id"] = str(comentario.id)
    comentario_dict["libro_id"] = str(comentario.libro_id)
    comentario_dict["fecha"] = comentario.fecha.isoformat() if isinstance(comentario.fecha, date) else str(comentario.fecha)

    comentarios.append(comentario_dict)
    escribir_csv(comentarios)
    return comentario

def actualizar_comentario(id: int, comentario: Comentario):
    comentarios = leer_csv()
    for i, c in enumerate(comentarios):
        if int(c["id"]) == id:
            comentario_dict = comentario.dict()
            comentario_dict["id"] = str(id)
            comentario_dict["libro_id"] = str(comentario.libro_id)
            comentario_dict["fecha"] = comentario.fecha.isoformat() if isinstance(comentario.fecha, date) else str(comentario.fecha)
            comentarios[i] = comentario_dict
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

def buscar_comentarios_por_libro(libro_id: int) -> List[dict]:
    return [c for c in leer_csv() if int(c["libro_id"]) == libro_id]
