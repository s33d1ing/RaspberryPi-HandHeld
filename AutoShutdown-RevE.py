#*************************************************************************
#
# autoshutdown.py  -  by: Chris Duerden (modified by Garrett Dees)
# Raspberry Pi safe shutdown program to interface with ATTiny85
# 9/8/2015      RevA - Initial Release
# 9/28/2015     RevB - Removed ", pull_up_down = GPIO.PUD_UP" from input
# 8/16/2017     RevC - Use ES's method of shutdown so metadata is saved
# 5/18/2018     RevD - Added pin for NESPi case mod, removed unused GPIO
# 10/11/2018    RevE - Removed NESPi pin and commented shutdown command
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
GPIO.setup(18, GPIO.IN)	# Set GPIO18 as input

# Define Program to shutdown RPi
def shutdown(pin):
    os.system("touch /tmp/es-shutdown && chown pi:pi /tmp/es-shutdown")
    os.system("killall emulationstation")

# Setup Interrupt on GPIO18 when Grounded
GPIO.add_event_detect(18, GPIO.FALLING, callback = shutdown, bouncetime = 200)

# Main
while 1:
    time.sleep(1)	# Prevent Program for ending only
