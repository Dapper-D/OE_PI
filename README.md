## 💾 Download & Install
**[👉 Download the latest GhostHID_Installer.exe here](https://github.com/Dapper-D/GhostHID/releases/latest)**

# 👻 GhostHID: The Human-Centric Peripheral Emulator

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Platform: Raspberry Pi Zero](https://img.shields.io/badge/Platform-Raspberry%20Pi%20Zero-red.svg)](https://www.raspberrypi.com/)
[![Status: Alpha](https://img.shields.io/badge/Status-Alpha-orange.svg)]()

**GhostHID** is an open-source hardware emulation framework that transforms a Raspberry Pi Zero into a high-fidelity USB HID (Human Interface Device). Unlike standard "mouse jigglers," GhostHID utilizes kernel-level spoofing and stochastic behavioral modeling to simulate a real human operator.

---

## 🛡️ The GhostHID Advantage

Standard activity monitors (Citrix, VMware, Teams) increasingly flag programmatic patterns. GhostHID bypasses these via:

* **Kernel-Level Spoofing:** Operates via Linux `ConfigFS`, presenting a genuine **Logitech VID/PID** to the host BIOS/OS.
* **Stochastic Typing:** Implements a "Micro-Typo" engine that simulates human fatigue, variable WPM, and real-time backspace corrections.
* **Bezier-Curve Kinematics:** Mouse movements follow non-linear paths with organic acceleration/deceleration, avoiding the "robotic straight line" trap.
* **Temporal Logic:** Follows a randomized 9-to-5 schedule, including staggered "lunch breaks" and "thinking pauses."

---

## 🏗️ System Architecture

GhostHID operates as a multi-layered ecosystem to ensure total separation between the simulation and the host machine.

* **The Pen (`generator.py`):** An offline utility that populates the library with contextually relevant professional notes.
* **The Script (`work_notes.txt`):** The raw data source for the simulation.
* **The Actor (`ghost_sim.py`):** The primary Python engine that translates text and coordinates into HID reports.
* **The Costume (`setup_hid.sh`):** The bash-level configuration that masks the Raspberry Pi as a consumer-grade peripheral.
* **The Director (`GhostHID_Installer.exe`):** A Windows-based utility for one-click deployment to the hardware.

---

## 📂 File Manifest

| File | Layer | Function |
| :--- | :--- | :--- |
| `setup_hid.sh` | **Hardware** | Initializes USB HID gadget mode & spoofs Device ID. |
| `generator.py` | **Data** | Generates professional-grade `work_notes.txt`. |
| `ghost_sim.py` | **Logic** | The main behavioral simulation engine. |
| `GhostHID_Installer.py` | **Deployment** | Remote setup script for non-technical users. |

---

## 🚀 Quick Start (Plug-and-Play)

### 1. Hardware Requirements
* **Raspberry Pi Zero** or **Zero 2 W**.
* **Micro-USB Data Cable** (Must support data transfer, not just charging).

### 2. Installation
1.  Connect the Pi to your computer via the **OTG/Data port**.
2.  Download the latest release of `GhostHID_Installer.exe`.
3.  Run the installer. It will automatically configure the Pi's kernel and start the service.

### 3. Manual Setup (Advanced)
If you prefer the command line:
```bash
git clone [https://github.com/](https://github.com/)[Your-Username]/GhostHID.git
cd GhostHID
sudo ./setup_hid.sh
python3 ghost_sim.py
```

🔍 Technical Deep-Dive

### Mouse Kinematics

GhostHID doesn't just "jump" pixels. It calculates a path using a **Cubic Bezier formula**:

$$
P(t) = (1-t)^3P_0 + 3(1-t)^2tP_1 + 3(1-t)t^2P_2 + t^3P_3
$$

This ensures that cursor movement has the natural **arc and jitter of a human hand**, making it difficult for "robot-detection" algorithms to identify.

---

### HID Reporting

By writing raw bytes directly to:
/dev/hidg0 # keyboard
/dev/hidg1 # mouse


GhostHID bypasses the OS's **software input stack entirely**.  
The host PC receives interrupts at the **hardware level**, making the device appear indistinguishable from a physical **Logitech keyboard or mouse**.

---

## ⚠️ Disclaimer

This project is intended **for educational and research purposes only**.

GhostHID explores the intersection of:

- Hardware emulation
- Behavioral analytics
- Human-like automation

Use of this tool **may violate workplace or institutional policies**.  
The developers assume **no liability for misuse**.

---

## 🤝 Contributing

We are actively seeking contributors from several domains:

**Mathematicians**  
Improve and refine organic cursor movement algorithms.

**Kernel Hackers**  
Expand the library of spoofed USB descriptors and improve HID gadget support.

**Beta Testers**  
Verify compatibility across different remote desktop clients.
