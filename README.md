GhostHID: The Human-Centric Peripheral Emulator.
 GhostHID is an open-source hardware simulation tool designed to bypass advanced activity monitoring systems (like those found in remote desktop environments like Citrix or VMware).
 
## 🏗️ How it Works: The Three-Layer System

1.  **The Hardware Layer (`setup_hid.sh`):** Configures the Linux kernel to "spoof" a real USB peripheral. It creates `/dev/hidg0` (Keyboard) and `/dev/hidg1` (Mouse).
2.  **The Data Layer (`generator.py`):** Creates a library of 50+ professional-sounding "Work Notes" (AWS, Cloud, Project Management) so the typing looks contextually relevant.
3.  **The Logic Layer (`ghost_sim.py`):** The "brain." It reads the notes, calculates human-like typing speeds, injects typos/corrections, and moves the mouse using non-linear math.

## 📂 File Manifest

| File | Purpose |
| :--- | :--- |
| `setup_hid.sh` | Run once at boot to enable USB Keyboard/Mouse mode. |
| `generator.py` | Run on your PC to generate the `work_notes.txt` file. |
| `ghost_sim.py` | The main script that runs the simulation loop. |
| `work_notes.txt` | The database of text the Pi will "type" throughout the day. |

## 🚀 Installation & Usage

1. **Hardware:** Use a Raspberry Pi Zero (or Zero 2 W) connected via the **Data/OTG** micro-USB port to the work PC.
2. **Setup:** Run `sudo ./setup_hid.sh` to initialize the HID ports.
3. **Run:** Execute `python3 ghost_sim.py`. The Pi will now wait for your "Shift Start" time and begin activity.

Unlike software-based "jigglers" or basic Arduinos, GhostHID transforms a Raspberry Pi Zero into a legitimate, hardware-level USB Human Interface Device (HID). It doesn't just "move the mouse"; it emulates human behavior.

🛠️ Why GhostHID?
Most enterprise monitoring "robots" flag activity that looks programmatic. GhostHID solves this by operating at the kernel level with:

Hardware Spoofing: Identifies as a standard consumer peripheral (e.g., a Logitech Keyboard or Dell Mouse) using custom Vendor IDs (VID) and Product IDs (PID).

Variable Keystroke Dynamics: Types text with randomized delays and "human-error" simulations (mistyping and backspacing).

Non-Linear Mouse Movement: Uses Bezier Curves to move the cursor smoothly across the screen, avoiding the "pixel-perfect" straight lines that trip modern detectors.

Workday Logic: Supports "shift patterns," including randomized start/end times and lunch breaks.

🚀 How It Works
GhostHID uses the Linux libcomposite driver to configure the Raspberry Pi Zero's OTG port. To your computer, the Pi is indistinguishable from a physical USB device plugged into the tower.

Current Features
[Planned] Ghost-Typewriter: Feeds professional "brainstorming" notes or documentation into any text editor at a natural WPM.

[Planned] Organic Jitter: Small, erratic mouse movements that simulate a hand resting on a mouse or shifting a window.

[Planned] Profile Switching: Toggle between "Deep Work" (typing-heavy) and "Research" (mouse-heavy) modes.

📂 Project Structure
setup_hid.sh: The core bash script to initialize USB Gadget mode on the Pi.

ghost_sim.py: The Python engine handling the "Human Logic."

notes/: A directory for pre-generated text snippets to be typed out.

⚠️ Disclaimer
This project is for educational and research purposes only. The goal is to explore the limits of HID emulation and hardware-level automation. Use responsibly and in accordance with your local policies and agreements.

🤝 Contributing
This is a community-driven project.im looking for:

Mathematicians to improve our Bezier curve mouse movements.

Linux Kernel Enthusiasts to expand USB descriptor options.

UI/UX Designers to create a simple web interface for the Pi.

