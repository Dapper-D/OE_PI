import time
import random
import datetime

def send_report(report, device="/dev/hidg0"):
    with open(device, 'rb+') as fd:
        fd.write(report)

def human_type_random():
    # Types random 'work-like' characters with human delays
    for _ in range(random.randint(10, 50)):
        key = random.randint(4, 29) # a-z
        send_report(bytes((0, 0, key, 0, 0, 0, 0, 0))) # Press
        send_report(bytes((0,)*8)) # Release
        time.sleep(random.uniform(0.1, 0.4))
        
        # 2% Typo chance
        if random.random() < 0.02:
            send_report(bytes((0, 0, 42, 0, 0, 0, 0, 0))) # Backspace

def organic_mouse():
    # Move mouse in a small jittery pattern
    for _ in range(random.randint(5, 20)):
        x, y = random.randint(-2, 2), random.randint(-2, 2)
        send_report(bytes((0, x, y, 0)), "/dev/hidg1")
        time.sleep(0.1)

if __name__ == "__main__":
    while True:
        now = datetime.datetime.now().time()
        # Active hours: 9 AM to 5 PM
        if datetime.time(9,0) <= now <= datetime.time(17,0):
            organic_mouse()
            if random.random() < 0.3: # 30% chance to type something
                human_type_random()
            time.sleep(random.randint(30, 90)) # Wait between actions
        else:
            time.sleep(600) # Sleep longer after hours
