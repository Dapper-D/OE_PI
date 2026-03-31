# 👻 GhostHID: The Human-Centric Peripheral Emulator
**### 🔨 Building from Source
If you want to compile the `.exe` yourself, run:
`pip install pyinstaller paramiko`

Then run:
`python -m PyInstaller --onefile --name "GhostHID_Installer" --add-data "src/setup_hid.sh;src" --add-data "src/ghost_sim.py;src" --clean scripts/GhostHID_Installer.py`

Then goto your dist/ folder**

**[👉 Download the latest GhostHID_Installer.exe here](https://github.com/Dapper-D/GhostHID/releases/latest)**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Platform: Raspberry Pi Zero](https://img.shields.io/badge/Platform-Raspberry%20Pi%20Zero-red.svg)](https://www.raspberrypi.com/)
[![Status: Alpha](https://img.shields.io/badge/Status-Alpha-orange.svg)]()

**GhostHID** is an open-source hardware emulation framework that transforms a Raspberry Pi Zero into a high-fidelity USB HID (Human Interface Device). Unlike standard "mouse jigglers," GhostHID utilizes kernel-level spoofing and stochastic behavioral modeling to simulate a real human operator.

---

## 🛡️ The GhostHID Advantage

Standard activity monitors (Citrix, VMware, Teams) increasingly flag programmatic patterns. GhostHID bypasses these via:

* **Hardware Obfuscation:** Generates a **unique 16-digit Serial Number** per device. Presenting a genuine **Logitech VID/PID** to the host BIOS/OS, it avoids "corporate fingerprinting."
* **Stochastic Typing:** Implements a "Micro-Typo" engine that simulates human fatigue, variable WPM, and real-time backspace corrections.
* **Bezier-Curve Kinematics:** Mouse movements follow non-linear paths with organic acceleration/deceleration, avoiding the "robotic straight line" trap.
* **Dynamic Scheduling:** Follows your specific 9-to-5 schedule via a `config.ini` file, including staggered "lunch breaks" and "thinking pauses."

---

## 🏗️ System Architecture

GhostHID operates as a multi-layered ecosystem to ensure total separation between the simulation and the host machine.

* **The Director (`GhostHID_Installer.exe`):** A Windows-based utility for one-click deployment. It handles SSH security, generates unique hardware IDs, and pushes your custom schedule to the Pi.
* **The Actor (`ghost_sim.py`):** The primary Python engine that translates text and coordinates into HID reports based on your `config.ini`.
* **The Costume (`setup_hid.sh`):** The bash-level configuration that masks the Raspberry Pi as a consumer-grade Logitech peripheral.

---

## 📂 File Manifest

| File | Layer | Function |
| :--- | :--- | :--- |
| `setup_hid.sh` | **Hardware** | Initializes USB HID gadget mode & spoofs Device ID with unique Serial. |
| `ghost_sim.py` | **Logic** | The main behavioral simulation engine with schedule awareness. |
| `config.ini` | **User Data** | Stores your custom shift and lunch hours. |
| `GhostHID_Installer.py` | **Deployment** | Remote setup script, password rotator, and ID generator. |

---

## 🚀 Quick Start (Alpha Testing)

### 1. Hardware Requirements
* **Raspberry Pi Zero** (v1.3, W, or 2 W).
* **Micro-USB DATA Cable** (Must support data transfer. If the installer can't find your Pi, try a different cable!).

### 2. Automated Installation
1. Connect the Pi to your computer via the **OTG/Data port** (the inner-most micro-USB port).
2. Download the latest `GhostHID_Installer.exe`.
3. Run the installer. You will be prompted to:
   * **Set your Shift Times:** (e.g., 09:00 to 17:00).
   * **Set a New Password:** Secures your Pi from unauthorized network access.
4. The installer will generate a **Unique Serial Number**, flash the kernel, and start the service.

### 3. ⚠️ The "Notepad" Rule
**IMPORTANT:** GhostHID types into whatever window is currently active. For the best experience, keep a **blank Notepad** or **Draft Email** open and in focus when you walk away from your desk.

---

## 🔧 Troubleshooting

| Issue | Potential Fix |
| :--- | :--- |
| **Installer can't find Pi** | Ensure you are using the **OTG port**, not the Power port. Swap your USB cable; many are "charge-only." |
| **Device not recognized** | Unplug and replug the Pi once setup is complete. The Windows driver (RNDIS) may need a refresh to see the new Logitech identity. |
| **Not typing/moving** | Check your `config.ini` on the Pi. The device will remain "dormant" if it is outside of your defined work hours or during "lunch." |

---

## 🔍 Technical Deep-Dive

### Mouse Kinematics

GhostHID doesn't just "jump" pixels. It calculates a path using a **Cubic Bezier formula**:

$$P(t) = (1-t)^3P_0 + 3(1-t)^2tP_1 + 3(1-t)t^2P_2 + t^3P_3$$

This ensures that cursor movement has the natural **arc and jitter of a human hand**, making it difficult for "robot-detection" algorithms to identify.

---

### HID Reporting

By writing raw bytes directly to:
* `/dev/hidg0` # keyboard
* `/dev/hidg1` # mouse

GhostHID bypasses the OS's **software input stack entirely**. The host PC receives interrupts at the **hardware level**, making the device appear indistinguishable from a physical **Logitech keyboard or mouse**.

---

## ⚠️ Disclaimer

This project is intended **for educational and research purposes only**. Use of this tool **may violate workplace or institutional policies**. The developers assume **no liability for misuse**.

---

## 🤝 Contributing & Feedback

We are actively seeking contributors and testers:

**Beta Testers** Verify compatibility across different remote desktop clients and report results in our **[Hardware Compatibility Megathread](https://github.com/Dapper-D/GhostHID/issues)**.

**Mathematicians** Improve and refine organic cursor movement algorithms.

**Kernel Hackers** Expand the library of spoofed USB descriptors and improve HID gadget support.
