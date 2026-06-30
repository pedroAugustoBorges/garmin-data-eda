from pathlib import Path

ROOT_PROJECT = Path (__file__).parent.parent

DATA_PATH = ROOT_PROJECT / "data"

RAW_DATA = ROOT_PROJECT / DATA_PATH / "raw" 

PROCESSED_DATA = DATA_PATH / "processed"

