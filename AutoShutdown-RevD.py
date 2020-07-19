#*************************************************************************
#
# autoshutdown.py  -  by: Chris Duerden (modified by Garrett Dees)
# Raspberry Pi safe shutdown program to interface with ATTiny85
# 9/8/2015      RevA - Initial Release
# 9/28/2015     RevB - Removed ", pull_up_down = GPIO.PUD_UP" from input
# 8/16/2017     RevC - Use ES's method of shutdown so metadata is saved
# 5/18/2018     RevD - Added pin for NESPi case, removed unused GPIO23
#
# Function: This program is designed to safely shut down a Raspberry Pi
# when a GPIO pin is brought low by a power management circuit.
# 
#*************************************************************************

# Import
import RPi.GPIO as GPIO
import time
import os

# Setup
GPIO.setmode(GPIO.BCM)	# Set Pin numbers to GPIO numbering
GPIO.setup(18, GPIO.IN)	# Set GPIO18 as input (Used for SuperGameGirl)
GPIO.setup(24, GPIO.IN)	# Set GPIO24 as input (Used for NESPi case mod)

# Define Program to shutdown RPi
def shutdown(pin):
	#os.system("sudo shutdown -h now")
	os.system("touch /tmp/es-shutdown && chown pi:pi /tmp/es-shutdown")
	os.system("killall emulationstation")

# Setup Interrupt on GPIO18 when Grounded
GPIO.add_event_detect(18, GPIO.FALLING, callback = shutdown, bouncetime = 200)

# Setup Interrupt on GPIO24 when Powered
GPIO.add_event_detect(24, GPIO.RISING, callback = shutdown, bouncetime = 200)

# Main
while 1:
    time.sleep(1)	# Prevent Program for ending only
