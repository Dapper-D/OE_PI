#!/bin/bash
# Initialize USB Gadget Mode
modprobe libcomposite
cd /sys/kernel/config/usb_gadget/
mkdir -p ghosthid && cd ghosthid

# Spoof as a Logitech Device
echo 0x046d > idVendor  
echo 0xc31c > idProduct 
mkdir -p strings/0x409
echo "Logitech" > strings/0x409/manufacturer
echo "USB Keyboard/Mouse Combo" > strings/0x409/product

# Define Keyboard
mkdir -p functions/hid.usb0
echo 1 > functions/hid.usb0/protocol
echo 8 > functions/hid.usb0/report_length
echo -ne \\x05\\x01\\x09\\x06\\xa1\\x01\\x05\\x07\\x19\\xe0\\x29\\xe7\\x15\\x00\\x25\\x01\\x75\\x01\\x95\\x08\\x81\\x02\\x95\\x01\\x75\\x08\\x81\\x03\\x95\\x05\\x75\\x01\\x05\\x08\\x19\\x01\\x29\\x05\\x91\\x02\\x95\\x01\\x75\\x03\\x91\\x03\\x95\\x06\\x75\\x08\\x15\\x00\\x25\\x65\\x05\\x07\\x19\\x00\\x29\\x65\\x81\\x00\\xc0 > functions/hid.usb0/report_desc

# Define Mouse
mkdir -p functions/hid.usb1
echo 2 > functions/hid.usb1/protocol
echo 4 > functions/hid.usb1/report_length
echo -ne \\x05\\x01\\x09\\x02\\xa1\\x01\\x09\\x01\\xa1\\x00\\x05\\x09\\x19\\x01\\x29\\x03\\x15\\x00\\x25\\x01\\x95\\x03\\x75\\x01\\x81\\x02\\x95\\x01\\x75\\x05\\x81\\x03\\x05\\x01\\x09\\x30\\x09\\x31\\x15\\x81\\x25\\x7f\\x75\\x08\\x95\\x02\\x81\\x06\\xc0\\xc0 > functions/hid.usb1/report_desc

mkdir -p configs/c.1/strings/0x409
echo "Config 1" > configs/c.1/strings/0x409/configuration
ln -s functions/hid.usb0 configs/c.1/
ln -s functions/hid.usb1 configs/c.1/
ls /sys/class/udc > UDC
