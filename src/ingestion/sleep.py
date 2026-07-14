from src.config import RAW_DATA
from src.ingestion.loaders import load_excel

SLEEP_PATH = RAW_DATA / "sono"

def load_sono_fases():
    return load_excel(SLEEP_PATH / "sono_fases.xlsx")

def load_sono_movimento():
    return load_excel(SLEEP_PATH / "sono_movimento.xlsx")

def load_sono_resumo():
    return load_excel(SLEEP_PATH / "sono_resumo.xlsx")

def load_sono_series():
    return load_excel(SLEEP_PATH / "sono_series.xlsx")