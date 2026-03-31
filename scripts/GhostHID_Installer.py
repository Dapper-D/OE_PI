import os
import sys
import paramiko
import random
import string

def resource_path(relative_path):
    """ Required for PyInstaller to find internal files """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def generate_serial(length=16):
    """ Avoids hardware fingerprinting by generating a unique Serial Number """
    return ''.join(random.choices(string.hexdigits.lower(), k=length))

def run_installer():
    print("--- 👻 GhostHID One-Click Setup (Alpha) ---")
    
    # 1. Gather User Preferences
    print("\n[🕒 SHIFT CONFIGURATION]")
    start = input("Start time? (e.g. 08:00): ")
    end = input("End time? (e.g. 16:30): ")
    lunch = input("Lunch time? (e.g. 12:00): ")

    # 2. Security Setup
    print("\n[🔐 SECURITY SETUP]")
    new_pw = input("Set a NEW password for your Pi: ")
    unique_serial = generate_serial()

    # 3. Create Config File locally
    with open("config.ini", "w") as f:
        f.write(f"[SHIFT]\nstart_time = {start}\nend_time = {end}\n")
        f.write(f"\n[LUNCH]\nlunch_start = {lunch}\nlunch_duration_minutes = 60\n")

    # 4. Deployment Logic
    pi_ip = "192.168.0.1" # Default for Pi Zero OTG
    user = "pi"
    default_pw = "raspberry"

    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        print(f"\n🚀 Connecting to GhostHID Hardware...")
        ssh.connect(pi_ip, username=user, password=default_pw, timeout=15)
        
        # Upload Files
        sftp = ssh.open_sftp()
        sftp.put(resource_path("src/setup_hid.sh"), '/home/pi/setup_hid.sh')
        sftp.put(resource_path("src/ghost_sim.py"), '/home/pi/ghost_sim.py')
        sftp.put("config.ini", '/home/pi/config.ini')
        sftp.close()

        # Execute Config
        print("⚙️ Applying spoofing and securing device...")
        commands = [
            f"echo '{user}:{new_pw}' | sudo chpasswd",
            f"sudo bash /home/pi/setup_hid.sh {unique_serial}",
            "echo 'dtoverlay=dwc2' | sudo tee -a /boot/config.txt"
        ]
        for cmd in commands:
            ssh.exec_command(cmd)

        print("\n" + "★"*40)
        print("🎉 SETUP COMPLETE!")
        print(f"Serial: {unique_serial}")
        print(f"New SSH Password: {new_pw}")
        print("-" * 40)
        print("⚠️  PRO-TIP: For the best results, keep a blank Notepad")
        print("   open and in focus. GhostHID will type into")
        print("   whatever window is currently active!")
        print("★"*40)

    except Exception as e:
        print(f"\n❌ FAILED: {e}")
        print("Check your Data Cable and ensure the Pi is in OTG mode.")

    if 'ssh' in locals(): ssh.close()
    input("\nPress Enter to Exit...")

if __name__ == "__main__":
    run_installer()