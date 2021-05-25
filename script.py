import datetime
import RPi.GPIO as GPIO

# https://sourceforge.net/p/raspberry-gpio-python/wiki/Examples/

# set constants (can set up to get user input later)
int_channel_input = 21 # change this to make work
int_channel_output = 22 # change this to make work

# pin numbering using board
GPIO.setmode(GPIO.BOARD)

# disable warnings
GPIO.setwarnings(False)

# configure a channel as an input (i.e., soil moisture sensor)
# https://sourceforge.net/p/raspberry-gpio-python/wiki/Inputs/
GPIO.setup(int_channel_input, GPIO.IN)

# configure a channel as an output (i.e., valve)
# https://sourceforge.net/p/raspberry-gpio-python/wiki/Outputs/
GPIO.setup(int_channel_out, GPIO.OUT)

# read the value of GPIO pin (i.e., get input)
GPIO.input(int_channel_input)

# set output state
GPIO.output(int_channel_out, state) # see documentation for possible values for state (State can be 0 / GPIO.LOW / False or 1 / GPIO.HIGH / True)

# clean up at end of script
GPIO.cleanup()




# print date
print(f'Practice Script: {datetime.datetime.today()}')