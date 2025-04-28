import csv
import os
from fastapi import HTTPException
from models.libro import Libro
from typing import List
from pathlib import Path

DATA_PATH = Path("data/libros.csv")
ELIMINADOS_PATH = Path("data/libros_eliminados.csv")

def leer_csv() -> List[dict]:
    if not DATA_PATH.exists():
        return []
    with open(DATA_PATH, newline='', encoding="utf-8") as f:
        return list(csv.DictReader(f))
    
def escribir_csv(libros: List[dict]):
    with open(DATA_PATH, 'w', newline='', encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "titulo", "autor_id", "anio_publicacion", "genero", "plataforma", "viral_en_tiktok"])
        writer.writeheader()
        writer.writerows(libros)

def listar_libros():
    return leer_csv()

def crear_libro(libro: Libro):
    libros = leer_csv()
    libro.id = max([int(l["id"]) for l in libros], default=0) + 1
    libros.append(libro.dict())
    escribir_csv(libros)
    return libro

def actualizar_libro(id: int, libro: Libro):
    libros = leer_csv()
    for i, l in enumerate(libros):
        if int(l["id"]) == id:
            libros[i] = libro.dict()
            libros[i]["id"] = str(id)
            escribir_csv(libros)
            return libro
    raise HTTPException(status_code=404, detail="Libro no encontrado")

def eliminar_libro(id: int):
    libros = leer_csv()
    libro_encontrado = None
    nuevos_libros = []
    for l in libros:
        if int(l["id"]) == id:
            libro_encontrado = l
        else:
            nuevos_libros.append(l)

    if not libro_encontrado:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    
    escribir_csv(nuevos_libros)
    with open(ELIMINADOS_PATH, 'a', newline='', encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=libro_encontrado.keys())
        if os.stat(ELIMINADOS_PATH).st_size == 0:
            writer.writeheader()
        writer.writerow(libro_encontrado)
    return {"mensaje": "Libro eliminado y registrado en historial."}

def filtrar_por_genero(genero: str):
    return [l for l in leer_csv() if l["genero"].lower() == genero.lower()]