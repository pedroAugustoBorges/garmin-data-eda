from src.config import RAW_DATA
from src.ingestion.loaders import load_excel

HRV_PATH = RAW_DATA / "hrv_recuperacao"

def load_endurance_score_hrv():
    return load_excel(HRV_PATH / "endurance_score.xlsx")

def load_hill_score_hrv():
    return load_excel(HRV_PATH / "hill_score.xlsx")