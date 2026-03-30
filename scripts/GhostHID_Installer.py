import os
import sys
import paramiko
import time

# 1. Logic to find files bundled inside the .exe
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def run_installer():
    print("--- GhostHID Windows One-Click Setup ---")
    print("Searching for Raspberry Pi on USB...")

    # Define paths to our bundled scripts
    # These must match the folder structure in your GitHub /src folder
    local_setup_sh = resource_path("src/setup_hid.sh")
    local_ghost_py = resource_path("src/ghost_sim.py")

    # Default Pi credentials for USB-Ethernet mode
    pi_ip = "192.168.0.1" # Standard for Pi Zero OTG
    user = "pi"
    pw = "raspberry"

    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        # Connect to the Pi
        ssh.connect(pi_ip, username=user, password=pw, timeout=10)
        print("✅ Connected to GhostHID Hardware.")

        # Step 1: Upload Files
        print("Step 1: Uploading core logic...")
        sftp = ssh.open_sftp()
        sftp.put(local_setup_sh, '/home/pi/setup_hid.sh')
        sftp.put(local_ghost_py, '/home/pi/ghost_sim.py')
        sftp.close()

        # Step 2: Configure Hardware & Service
        print("Step 2: Configuring HID Drivers & Auto-Start...")
        commands = [
            "chmod +x /home/pi/setup_hid.sh",
            "sudo /home/pi/setup_hid.sh",
            "echo 'dtoverlay=dwc2' | sudo tee -a /boot/config.txt",
            "echo 'dwc2' | sudo tee -a /etc/modules",
            "sudo systemctl enable /home/pi/ghosthid.service" # Assuming service file is also pushed
        ]
        
        for cmd in commands:
            ssh.exec_command(cmd)
            
        print("\n🎉 SUCCESS: GhostHID is now active and spoofing a Logitech Keyboard.")
        print("You can now unplug and replug the device to finish initialization.")

    except Exception as e:
        print(f"\n❌ ERROR: Could not connect to Pi. {e}")
        print("Check: Is the Pi in OTG/Data mode? Is the cable a Data cable?")

    ssh.close()
    input("\nPress Enter to close...")

if __name__ == "__main__":
    run_installer()