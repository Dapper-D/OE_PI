import time
import random
import datetime
import configparser
import os

# --- Configuration Loading ---
config = configparser.ConfigParser()
# Path assumes config.ini is in the same folder on the Pi
config_path = os.path.join(os.path.dirname(__file__), 'config.ini')
config.read(config_path)

def get_time_obj(time_str):
    try:
        return datetime.datetime.strptime(time_str, "%H:%M").time()
    except:
        return datetime.datetime.strptime("09:00", "%H:%M").time()

# Fallback defaults if config is missing
SHIFT_START = get_time_obj(config.get('SHIFT', 'start_time', fallback="09:00"))
SHIFT_END = get_time_obj(config.get('SHIFT', 'end_time', fallback="17:00"))
LUNCH_START = get_time_obj(config.get('LUNCH', 'lunch_start', fallback="12:00"))
LUNCH_DURATION = int(config.get('LUNCH', 'lunch_duration_minutes', fallback="60"))

def is_work_time():
    now = datetime.datetime.now().time()
    
    # 1. Check Shift Bounds
    if not (SHIFT_START <= now <= SHIFT_END):
        return False
        
    # 2. Check Lunch Break
    lunch_dt = datetime.datetime.combine(datetime.date.today(), LUNCH_START)
    lunch_end_dt = lunch_dt + datetime.timedelta(minutes=LUNCH_DURATION)
    
    if lunch_dt.time() <= now <= lunch_end_dt.time():
        return False
        
    return True

def simulate_activity():
    """Placeholder for the HID injection logic (Keyboard/Mouse)"""
    # In the real hardware version, this writes to /dev/hidg0 and /dev/hidg1
    actions = ["Typing work note...", "Moving mouse (Bezier)...", "Micro-jittering..."]
    print(f"[{datetime.datetime.now().time()}] {random.choice(actions)}")

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