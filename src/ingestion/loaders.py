from pathlib import Path
import pandas as pd

def load_excel(path : Path):
    if not path.exists():
        raise FileNotFoundError(f"{path} not found")
    
    return pd.read_excel(path)