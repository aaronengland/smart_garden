import datetime
import RPi.GPIO as GPIO
import time

# https://sourceforge.net/p/raspberry-gpio-python/wiki/Examples/

# input GPIO pin
int_channel_input = 40
# output GPIO pin
int_channel_output = 15

# pin numbering using board
GPIO.setmode(GPIO.BOARD)
# disable warnings
GPIO.setwarnings(False)

# configure a channel as an input (i.e., soil moisture sensor)
# https://sourceforge.net/p/raspberry-gpio-python/wiki/Inputs/
GPIO.setup(int_channel_input, GPIO.IN)
# configure a channel as an output
GPIO.setup(int_channel_output, GPIO.OUT)

# get initial value (1 == dry)
int_moisture_level = GPIO.input(int_channel_input)
# print
print('Initial Moisture Level: {0}'.format(int_moisture_level))

# begin while loop
while True:
    # logic to check if mositure level is dry
    if int_moisture_level == 1: # dry
        # print
        print('Soil is dry, turning valve on...')
        # turn on valve
        GPIO.output(int_channel_output, 1) # set to 1 for ON
        # while sensor is dry
        while int_moisture_level == 1:
            # get measurement
            int_moisture_level = GPIO.input(int_channel_input)
            # logic
            if int_moisture_level == 1:
                str_moisture_level = 'Dry'
            elif int_moisture_level == 0:
                str_moisture_level = 'Wet'
            # print level
            print('Moisture Level: {0}'.format(str_moisture_level))
            # sleep
            time.sleep(1)
        # turn off valve
        GPIO.output(int_channel_output, 0)
        # print message
        print('Soil is wet, valve is off.')
        # sleep
        time.sleep(30)
    else:
        time.sleep(30)
