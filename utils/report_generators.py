import json
import datetime
import os

def log_result_to_file(data, filename="test_log.json"):
    timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    os.makedirs("reports", exist_ok=True)
    path = f"reports/{filename.replace('.json', '')}_{timestamp}.json"
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    return path

def write_simple_log(message, log_file="test_log.txt"):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, "a") as f:
        f.write(f"[{timestamp}] {message}\n")
