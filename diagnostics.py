# diagnostics.py
import time
import platform
import socket
from typing import Any, Dict

APP_START = time.time()

def collect_report(config: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "app_name": config.get("app_name", "portfolio-flask-starter"),
        "focus": config.get("focus", "A"),
        "hostname": socket.gethostname(),
        "python_version": platform.python_version(),
        "since_start_seconds": round(time.time() - APP_START, 2),
        "notes": "Skeleton report. Implement focus-specific checks later."
    }
