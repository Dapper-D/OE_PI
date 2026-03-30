# GhostHID: The Human-Centric Peripheral Emulator

GhostHID is an open-source hardware simulation tool that turns a Raspberry Pi Zero into a USB keyboard and mouse device capable of producing realistic human-like activity.

## Why GhostHID?

Unlike software-based mouse jigglers or simple Arduino scripts, GhostHID operates as a hardware-level USB Human Interface Device (HID).

* **Hardware Spoofing:** Appears as a normal consumer keyboard and mouse by using custom Vendor IDs (VID) and Product IDs (PID).
* **Variable Keystroke Dynamics:** Uses randomized typing speed, delays, typos, and corrections to simulate real typing behavior.
* **Non-Linear Mouse Movement:** Uses Bezier curves instead of straight-line cursor movement.
* **Workday Logic:** Supports shift schedules, randomized start and end times, and lunch breaks.

## How It Works

GhostHID uses a three-layer system:

1. **Hardware Layer (`setup_hid.sh`)**

   * Configures the Raspberry Pi in USB Gadget mode.
   * Creates `/dev/hidg0` for keyboard input.
   * Creates `/dev/hidg1` for mouse input.

2. **Data Layer (`generator.py`)**

   * Generates a library of 50+ professional-sounding work notes.
   * Produces `work_notes.txt`, which is used as the source of typed text.

3. **Logic Layer (`ghost_sim.py`)**

   * Controls typing speed, pauses, typos, corrections, and mouse movement.
   * Reads from `work_notes.txt` and performs the simulation loop.

## File Manifest

| File             | Purpose                                         |
| ---------------- | ----------------------------------------------- |
| `setup_hid.sh`   | Initializes USB keyboard and mouse gadget mode. |
| `generator.py`   | Generates the `work_notes.txt` file.            |
| `ghost_sim.py`   | Main simulation engine and control loop.        |
| `work_notes.txt` | Source text typed during the simulation.        |

## Installation & Usage

1. Connect a Raspberry Pi Zero or Raspberry Pi Zero 2 W to the target computer using the Data/OTG USB port.
2. Initialize the HID device:

```bash
sudo ./setup_hid.sh
```

3. Start the simulator:

```bash
python3 ghost_sim.py
```

4. The simulator will wait until the configured shift start time and then begin generating activity.

## Example Runtime Flow

1. The target computer detects the Raspberry Pi as a keyboard and mouse.
2. `ghost_sim.py` checks the current time.
3. When the configured work period begins, it selects a note from `work_notes.txt`.
4. Starts by 9am, automatically "logs off" after 5 PM and "takes lunch" at noon.
5. Mouse movement data is written to `/dev/hidg1`.
6. Keyboard data is written to `/dev/hidg0`.
7. The loop repeats with randomized timing and movement patterns.

## Current Features

* USB HID keyboard and mouse emulation
* Human-like typing delays and corrections
* Professional note generation
* Bezier-curve mouse movement
* Configurable workday scheduling
* Randomized shift start, end, and break times

## Planned Features

* **Ghost-Typewriter:** Improved note generation for brainstorming and documentation.
* **Organic Jitter:** Small erratic mouse movements that simulate a hand resting on a mouse.
* **Profile Switching:** Toggle between typing-heavy and mouse-heavy behavior profiles.
* **Expanded USB Profiles:** Additional keyboard and mouse descriptor options.
* **Web Interface:** A simple browser-based interface for configuring the Raspberry Pi.

## Disclaimer

This project is for educational and research purposes only. The goal is to explore the limits of HID emulation and hardware-level automation. Use responsibly and in accordance with your local laws, workplace policies, and agreements.

## Contributing

GhostHID is a community-driven project. Contributions are welcome in the following areas:

* Mathematicians to improve Bezier curve mouse movement.
* Linux kernel enthusiasts to expand USB descriptor options.
* UI/UX designers to create a simple web interface for the Raspberry Pi.
* Python developers to improve the simulation engine and note generation.
