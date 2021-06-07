from functions import interval_watering

# https://sourceforge.net/p/raspberry-gpio-python/wiki/Examples/

# input GPIO pin
int_channel_input = 40
# output GPIO pin
int_channel_output = 15
# seconds to wait if soil dry
int_sec_sleep_dry = 1
# seconds to wait of soil is wet
int_sec_sleep_wet = 10

# run function
interval_watering(int_channel_input=int_channel_input, 
                  int_channel_output=int_channel_output, 
                  int_sec_sleep_dry=int_sec_sleep_dry, 
                  int_sec_sleep_wet=int_sec_sleep_wet)
