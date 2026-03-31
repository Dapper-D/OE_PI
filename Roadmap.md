Phase 1: Connectivity & Reliability (Current)
[ ] Fix "Active Window" issue: Investigate if Pi can detect window focus (Challenge: USB HID is one-way).

[ ] Workaround: Add a 10-second "Safety Delay" after the Pi starts before it begins typing.

Phase 2: Organic Behavior Expansion
[ ] The "Lunch Break" Protocol: Add a 1-hour block of zero activity at a randomized time between 12:00 PM and 1:30 PM.

[ ] The "Hand Jitter" Mode: Implement 1-2 pixel micro-movements every 30 seconds to simulate a hand resting on the mouse.

Phase 3: User Interface (The "Hand-Hold" Level Up)
[ ] Web Dashboard: Host a simple local website on the Pi so users can change their "Shift Times" from their phone via Wi-Fi.

[ ] Profile Toggling: Create "Meeting Mode" (Mouse only) vs "Work Mode" (Keyboard + Mouse).

🏁 Final Instructions
The "Active Window" Problem: For now, I've added a warning in the Disclaimer section of the README (done in the previous step). The 10-second safety delay is a good "Roadmap" fix.

Re-pack the EXE: Use the same PyInstaller command we discussed. It will now bundle the updated setup_hid.sh.