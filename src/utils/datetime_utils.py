import math
import datetime
from datetime import timedelta

def to_hour_label(min):
    
    minutes = math.floor(min)
    hour, minute = divmod(minutes, 60)
    return f"{hour:02d}:{minute:02d}"