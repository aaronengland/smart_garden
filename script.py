import datetime
import RPi.GPIO as GPIO
import time
#import pandas as pd

# https://sourceforge.net/p/raspberry-gpio-python/wiki/Examples/

# set constants (can set up to get user input later)
#int_channel_output = 22 # change this to make work

# define function to test input
def test_input(int_channel_input=40, int_sec_sleep=2, int_thresh_n_rounds_wet=10):
    # pin numbering using board
    GPIO.setmode(GPIO.BOARD)
    # disable warnings
    GPIO.setwarnings(False)
    # configure a channel as an input (i.e., soil moisture sensor)
    # https://sourceforge.net/p/raspberry-gpio-python/wiki/Inputs/
    GPIO.setup(int_channel_input, GPIO.IN)
    # instantiate n round Wet
    int_n_rounds_wet = 0
    # instantiate empty list
    list_str_output = []
    # continuously run
    while int_n_rounds_wet < int_thresh_n_rounds_wet:
        # read the value of GPIO pin (i.e., get input; 1==Dry, 0==Wet)
        int_input_val = GPIO.input(int_channel_input)
        # logic
        if int_input_val == 0:
            str_input_val = 'Wet'
            int_n_rounds_wet += 1
        elif int_input_val == 1:
            str_input_val = 'Dry'
        # save string
        str_output = 'Water Level: {0}; Wet for {1} rounds.'.format(str_input_val, int_n_rounds_wet)
        # print value
        print(str_output)
        # append string to list
        list_str_output.append(str_output)
        # rest int_sec_sleep seconds
        time.sleep(int_sec_sleep)
    # cleanup
    GPIO.cleanup()
    # return
    return list_str_output

# run function
list_str_output = test_input(int_channel_input=40,
                             int_sec_sleep=2,
                             int_thresh_n_rounds_wet=10)

# print list
print(list_str_output)


# configure a channel as an output (i.e., valve)
# https://sourceforge.net/p/raspberry-gpio-python/wiki/Outputs/
#GPIO.setup(int_channel_out, GPIO.OUT)

# set initial input to 
#int_input_val
   
# set output state
#GPIO.output(int_channel_out, state) # see documentation for possible values for state (State can be 0 / GPIO.LOW / False or 1 / GPIO.HIGH / True)
