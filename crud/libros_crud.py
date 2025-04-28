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