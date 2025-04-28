import csv
import os
from fastapi import HTTPException
from models.libro import Libro
from typing import List
from pathlib import Path

DATA_PATH = Path("data/libros.csv")
ELIMINADOS_PATH = Path("data/libros_eliminados.csv")