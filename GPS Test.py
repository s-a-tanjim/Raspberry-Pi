#NEO 6m v2 GPS with Raspberry Pi 3 B+

import time
import serial
import string
import pynmea2
import RPi.GPIO as gpio
gpio.setmode(gpio.BCM)

port="/dev/ttyAMA0"

ser=serial.Serial(port,baudrate = 9600, timeout= 0.5)
try:
    while 1:
        try:
            data=ser.readline()
        except:
            print("Loading")
            
        
        if data[0:6]=='$GPGGA':
            msg=pynmea2.parse(data)
            latval=msg.lat
            concatlat="Lat: "+str(latval)
            print(concatlat)
            
            longval=msg.lon
            concatlong="Long: "+str(longval)
            print(concatlong)
            
            time.sleep(5)
            
except KeyboardInterrupt:
    time.sleep(2)
    
	
	

# gps connection:
#	VCC-> 5v/3.3v	GND->GND
#	TXD-> GPIO 15 (RXD of Pi)
#	RXD-> GPIO 14 (TXD of Pi)


# Pi Config:
#	sudo apt-get update && apt-get upgrade
#	sudo nano /boot/config.txt
#		#Add those lines at the bottom of the file...
#		dtoverlay=pi3-disable-bt
#		core_freq=250
#		enable_uart=1
#		force_turbo=1
#		#save file   ^x->y->enter
#	sudo cp /boot/cmdline.txt /boot/cmdline.txt.backup	#make a backup of cmdline.txt
#	sudo nano /boot/cmdline.txt
#		remove "console=serial0,115200"
#		and modify "root=PARTUUID=d27d14ee-02" to "root=/dev/mmcblk0p2"
#		#save file   ^x->y->enter
#	sudo reboot
#	sudo systemctl stop serial-getty@ttyS0.service
#	sudo systemctl disable serial-getty@ttyS0.service
#	sudo reboot
#	sudo systemctl enable serial-getty@ttyAMA0.service
#	ls -l /dev  #to check serial0 -> ttyAMA0

#	sudo apt-get install minicom #to connect to the GPS module and make sense of data
#	sudo pip install pynmea2 #to convert gps data into readable data




# Way to execute:
#	sudo minicom -D /dev/ttyAMA0 -b 9600 for raw data (1) [sudo apt-get install minicom REQUIRED]
#	sudo cat /dev/ttyAMA0  for raw data (2)
