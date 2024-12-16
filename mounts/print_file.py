import time
from datetime import datetime

while True:
    with open("/data/current_time.txt", "w") as file:
        file.write(f"Current time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    time.sleep(5)