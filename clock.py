from datetime import datetime
import time

def digital_clock():
    while True:
        current_time = datetime.now().strftime("%H:%M:%S")
        print(current_time, end="\r")
        time.sleep(1)

if __name__ == "__main__":
    digital_clock() 