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