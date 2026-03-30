#!/bin/bash
# GhostHID - Core USB Initialization Script
# This script configures the Pi Zero as a Keyboard and Mouse.

# 1. Load the necessary driver
modprobe libcomposite

# 2. Create the gadget directory
cd /sys/kernel/config/usb_gadget/
mkdir -p ghosthid
cd ghosthid

# 3. Identity Spoofing (Change these to match a real device)
# 0x046d = Logitech, 0xc31c = Keyboard
echo 0x1d6b > idVendor  # Linux Foundation
echo 0x0104 > idProduct # Multifunction Composite Gadget
echo 0x0100 > bcdDevice # v1.0.0
echo 0x0200 > bcdUSB    # USB 2.0

# 4. Device Strings (What the PC sees in Device Manager)
mkdir -p strings/0x409
echo "fedcba9876543210" > strings/0x409/serialnumber
echo "Logitech" > strings/0x409/manufacturer
echo "USB Keyboard/Mouse Combo" > strings/0x409/product

# 5. Create Configurations
mkdir -p configs/c.1/strings/0x409
echo "Config 1: HID Gadget" > configs/c.1/strings/0x409/configuration
echo 250 > configs/c.1/bmAttributes # Max Power
echo 500 > configs/c.1/MaxPower

# 6. Add Keyboard Function
mkdir -p functions/hid.usb0
echo 1 > functions/hid.usb0/protocol
echo 1 > functions/hid.usb0/subclass
echo 8 > functions/hid.usb0/report_length
# This is the report descriptor for a standard 101-key keyboard
echo -ne \\x05\\x01\\x09\\x06\\xa1\\x01\\x05\\x07\\x19\\xe0\\x29\\xe7\\x15\\x00\\x25\\x01\\x75\\x01\\x95\\x08\\x81\\x02\\x95\\x01\\x75\\x08\\x81\\x03\\x95\\x05\\x75\\x01\\x05\\x08\\x19\\x01\\x29\\x05\\x91\\x02\\x95\\x01\\x75\\x03\\x91\\x03\\x95\\x06\\x75\\x08\\x15\\x00\\x25\\x65\\x05\\x07\\x19\\x00\\x29\\x65\\x81\\x00\\xc0 > functions/hid.usb0/report_desc
ln -s functions/hid.usb0 configs/c.1/

# 7. Add Mouse Function
mkdir -p functions/hid.usb1
echo 2 > functions/hid.usb1/protocol
echo 1 > functions/hid.usb1/subclass
echo 4 > functions/hid.usb1/report_length
# This is the report descriptor for a standard 3-button mouse
echo -ne \\x05\\x01\\x09\\x02\\xa1\\x01\\x09\\x01\\xa1\\x00\\x05\\x09\\x19\\x01\\x29\\x03\\x15\\x00\\x25\\x01\\x95\\x03\\x75\\x01\\x81\\x02\\x95\\x01\\x75\\x05\\x81\\x03\\x05\\x01\\x09\\x30\\x09\\x31\\x15\\x81\\x25\\x7f\\x75\\x08\\x95\\x02\\x81\\x06\\xc0\\xc0 > functions/hid.usb1/report_desc
ln -s functions/hid.usb1 configs/c.1/

# 8. Enable the gadget
ls /sys/class/udc > UDC
