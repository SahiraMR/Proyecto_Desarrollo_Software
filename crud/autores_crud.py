import csv
import os
from fastapi import HTTPException
from models.autor import Autor
from typing import List
from pathlib import Path

# Rutas de archivos
DATA_PATH = Path("data/autores.csv")
ELIMINADOS_PATH = Path("data/autores_eliminados.csv")