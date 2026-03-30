import time
import random
import datetime

# HID keycodes for standard characters
NULL_CHAR = bytes((0,)*8)
def type_key(key_code):
    with open('/dev/hidg0', 'rb+') as fd:
        # Press key
        fd.write(bytes((0, 0, key_code, 0, 0, 0, 0, 0)))
        # Release key
        fd.write(NULL_CHAR)

def move_mouse(x, y):
    with open('/dev/hidg1', 'rb+') as fd:
        # x, y are signed bytes (-127 to 127)
        fd.write(bytes((0, x, y, 0)))

def human_typing(text):
    for char in text:
        # Simple ASCII to HID mapping (Simplified for A-Z, space, and backspace)
        # 0x04 is 'a', 0x2c is space, etc.
        type_key(random.randint(4, 29)) # Just typing random junk to look like work
        time.sleep(random.uniform(0.1, 0.3))
        
        # 3% chance of a typo
        if random.random() < 0.03:
            type_key(40) # Enter/Error
            time.sleep(0.5)
            type_key(42) # Backspace

def workday_loop():
    while True:
        now = datetime.datetime.now().time()
        # Only active between 09:00 and 17:00
        if datetime.time(9,0) <= now <= datetime.time(17,0):
            # 1. Move Mouse "Organically"
            for _ in range(random.randint(10, 30)):
                move_mouse(random.randint(-2, 2), random.randint(-2, 2))
                time.sleep(0.1)
            
            # 2. Type a random note
            notes = open("work_notes.txt").readlines()
            human_typing(random.choice(notes))
            
            # 3. Random "Thinking" pause
            time.sleep(random.randint(60, 300))
        else:
            print("After hours. Sleeping...")
            time.sleep(1800)

if __name__ == "__main__":
    workday_loop()
