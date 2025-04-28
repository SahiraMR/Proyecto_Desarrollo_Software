import csv
import os
from fastapi import HTTPException
from models.comentario import Comentario
from typing import List
from pathlib import Path

# Rutas de archivos
DATA_PATH = Path("data/comentarios.csv")
ELIMINADOS_PATH = Path("data/comentarios_eliminados.csv")