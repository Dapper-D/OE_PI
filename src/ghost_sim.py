import time
import random
import datetime
import configparser
import os

# --- 1. Configuration Loading ---
config = configparser.ConfigParser()
config_path = os.path.join(os.path.dirname(__file__), 'config.ini')
config.read(config_path)

def get_time_obj(time_str):
    try:
        return datetime.datetime.strptime(time_str, "%H:%M").time()
    except:
        return datetime.datetime.strptime("09:00", "%H:%M").time()

SHIFT_START = get_time_obj(config.get('SHIFT', 'start_time', fallback="09:00"))
SHIFT_END = get_time_obj(config.get('SHIFT', 'end_time', fallback="17:00"))
LUNCH_START = get_time_obj(config.get('LUNCH', 'lunch_start', fallback="12:00"))
LUNCH_DURATION = int(config.get('LUNCH', 'lunch_duration_minutes', fallback="60"))

# --- 2. THE HARDWARE INTERFACE ---

def send_keyboard_report(report_bytes):
    """Writes 8-byte keyboard reports to /dev/hidg0"""
    try:
        with open('/dev/hidg0', 'rb+') as fd:
            fd.write(report_bytes)
    except FileNotFoundError:
        pass 

def send_mouse_report(buttons, x, y):
    """Writes 3-byte mouse reports to /dev/hidg1"""
    report = bytes([buttons, x & 0xff, y & 0xff])
    try:
        with open('/dev/hidg1', 'rb+') as fd:
            fd.write(report)
    except FileNotFoundError:
        pass 

# --- 3. THE HUMAN BEHAVIOR LOGIC ---

def move_mouse_humanly(dest_x, dest_y, steps=50):
    """Moves mouse using a Cubic Bezier path for organic feel."""
    cx = dest_x // 2 + random.randint(-20, 20)
    cy = dest_y // 2 + random.randint(-20, 20)
    last_x, last_y = 0, 0
    
    for i in range(1, steps + 1):
        t = i / steps
        target_x = int((1-t)**2 * 0 + 2*(1-t)*t * cx + t**2 * dest_x)
        target_y = int((1-t)**2 * 0 + 2*(1-t)*t * cy + t**2 * dest_y)
        rel_x = target_x - last_x
        rel_y = target_y - last_y
        
        send_mouse_report(0, rel_x, rel_y)
        last_x, last_y = target_x, target_y
        time.sleep(random.uniform(0.008, 0.015))

def is_work_time():
    now = datetime.datetime.now().time()
    if not (SHIFT_START <= now <= SHIFT_END):
        return False
    
    lunch_dt = datetime.datetime.combine(datetime.date.today(), LUNCH_START)
    lunch_end_dt = lunch_dt + datetime.timedelta(minutes=LUNCH_DURATION)
    
    if lunch_dt.time() <= now <= lunch_end_dt.time():
        return False
    return True

def simulate_activity():
    """Triggers actual HID hardware events"""
    choice = random.choice(["move", "jitter", "scroll"])
    
    if choice == "move":
        # Random distance for the Bezier curve
        move_mouse_humanly(random.randint(-100, 100), random.randint(-100, 100))
    elif choice == "jitter":
        # Micro-movements
        for _ in range(5):
            send_mouse_report(0, random.randint(-1, 1), random.randint(-1, 1))
            time.sleep(0.1)
    elif choice == "scroll":
        # Using the mouse report to jiggle slightly
        send_mouse_report(0, 0, 1)
        time.sleep(0.2)
        send_mouse_report(0, 0, -1)

# --- 4. MAIN ENGINE LOOP ---

if __name__ == "__main__":
    print(f"GhostHID Engine Active. Monitoring shift: {SHIFT_START}-{SHIFT_END}")
    
    while True:
        if is_work_time():
            simulate_activity()
            # Random delay between 30 and 120 seconds to look human
            time.sleep(random.randint(30, 120))
        else:
            # Check every 5 minutes if shift has started
            time.sleep(300)