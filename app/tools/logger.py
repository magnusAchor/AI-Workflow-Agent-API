import json
from datetime import datetime

def log_step(step, output):
    log = {
        "step": step,
        "output": output,
        "timestamp": str(datetime.utcnow())
    }

    print(json.dumps(log))