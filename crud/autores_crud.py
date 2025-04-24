import csv
from pathlib import Path



DATA_PATH = Path("data/autores.csv")

def listar_autores():
    if not DATA_PATH.exists():
        return []
    with open(DATA_PATH, newline='', encoding="utf-8") as f:
        return list(csv.DictReader(f))


