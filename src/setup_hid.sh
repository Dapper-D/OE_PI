#!/bin/bash
# Accept Serial Number as the first argument from the installer
SERIAL_NUM=${1:-"fedcba9876543210"}

# Load the USB Gadget module
modprobe libcomposite

# Create the gadget configuration
cd /sys/kernel/config/usb_gadget/
mkdir -p ghosthid && cd ghosthid

# Identity Spoofing (Logitech K120 / Mouse Combo)
echo 0x046d > idVendor  # Logitech
echo 0xc31c > idProduct # Keyboard/Mouse Combo
echo 0x0100 > bcdDevice # Version 1.0.0
echo 0x0200 > bcdUSB    # USB 2.0

mkdir -p strings/0x409
echo "$SERIAL_NUM" > strings/0x409/serialnumber
echo "Logitech" > strings/0x409/manufacturer
echo "USB Keyboard/Mouse Combo" > strings/0x409/product

# Create the Configuration
mkdir -p configs/c.1/strings/0x409
echo "Config 1: HID Gadget" > configs/c.1/strings/0x409/configuration
echo 250 > configs/c.1/bmAttributes # Max power consumption
echo 100 > configs/c.1/bMaxPower

# --- Keyboard Descriptor (/dev/hidg0) ---
mkdir -p functions/hid.usb0
echo 1 > functions/hid.usb0/protocol
echo 1 > functions/hid.usb0/subclass
echo 8 > functions/hid.usb0/report_length
# Standard Keyboard Report Descriptor
echo -ne \\x05\\x01\\x09\\x06\\xa1\\x01\\x05\\x07\\x19\\xe0\\x29\\xe7\\x15\\x00\\x25\\x01\\x75\\x01\\x95\\x08\\x81\\x02\\x95\\x01\\x75\\x08\\x81\\x03\\x95\\x05\\x75\\x01\\x05\\x08\\x19\\x01\\x29\\x05\\x91\\x02\\x95\\x01\\x75\\x03\\x91\\x03\\x95\\x06\\x75\\x08\\x15\\x00\\x25\\x65\\x05\\x07\\x19\\x00\\x29\\x65\\x81\\x00\\xc0 > functions/hid.usb0/report_desc
ln -s functions/hid.usb0 configs/c.1/

# --- Mouse Descriptor (/dev/hidg1) ---
mkdir -p functions/hid.usb1
echo 2 > functions/hid.usb1/protocol
echo 1 > functions/hid.usb1/subclass
echo 4 > functions/hid.usb1/report_length
# Standard Mouse Report Descriptor
echo -ne \\x05\\x01\\x09\\x02\\xa1\\x01\\x09\\x01\\xa1\\x00\\x05\\x09\\x19\\x01\\x29\\x03\\x15\\x00\\x25\\x01\\x95\\x03\\x75\\x01\\x81\\x02\\x95\\x01\\x75\\x05\\x81\\x03\\x05\\x01\\x09\\x30\\x09\\x31\\x15\\x81\\x25\\x7f\\x75\\x08\\x95\\x02\\x81\\x06\\xc0\\xc0 > functions/hid.usb1/report_desc
ln -s functions/hid.usb1 configs/c.1/

# Enable the gadget
ls /sys/class/udc > UDC

echo "✅ Hardware Identity successfully spoofed as Logitech with Serial: $SERIAL_NUM"