import datetime
import RPi.GPIO as GPIO
import time

# https://sourceforge.net/p/raspberry-gpio-python/wiki/Examples/

# input GPIO pin
int_channel_input = 40
# output GPIO pin
int_channel_output = 15
# seconds to wait if soil dry
int_sec_sleep_dry = 1
# seconds to wait of soil is wet
int_sec_sleep_wet = 10



# pin numbering using board
GPIO.setmode(GPIO.BOARD)
# disable warnings
GPIO.setwarnings(False)

# configure a channel as an input (i.e., soil moisture sensor)
# https://sourceforge.net/p/raspberry-gpio-python/wiki/Inputs/
GPIO.setup(int_channel_input, GPIO.IN)
# configure a channel as an output
GPIO.setup(int_channel_output, GPIO.OUT)

# begin while loop
while True:
    # get initial value (1 == dry)
    int_moisture_level = GPIO.input(int_channel_input)
    # print
    print('Initial Moisture Level: {0}'.format(int_moisture_level))
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
            # print level
            print('Sensor is dry, valve is on.')
            print('Checking moisture level again in {0} second(s).'.format(int_sec_sleep_dry))
            # sleep
            time.sleep(int_sec_sleep_dry)
        # turn off valve
        GPIO.output(int_channel_output, 0)
        # print message
        print('Sensor is wet, valve is off.')
        print('Checking moisture level again in {0} second(s).'.format(int_sec_sleep_wet))
        # sleep
        time.sleep(int_sec_sleep_wet)
    else:
        print('Sensor is wet, valve is off.')
        print('Checking moisture level again in {0} second(s).'.format(int_sec_sleep_wet))
        time.sleep(int_sec_sleep_wet)
