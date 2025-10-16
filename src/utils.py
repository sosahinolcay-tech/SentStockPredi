# src/utils.py
import json
from typing import Any

def to_serializable(obj: Any):
    """
    Helper for JSON serializing numpy / pandas objects if needed
    """
    try:
        import numpy as np
        if isinstance(obj, np.generic):
            return obj.item()
    except Exception:
        pass
    try:
        import pandas as pd
        if isinstance(obj, pd.Timestamp):
            return obj.isoformat()
    except Exception:
        pass
    raise TypeError("Type not serializable")