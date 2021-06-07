from functions import interval_watering
import features as feat

# run function
interval_watering(int_channel_input=feat.int_channel_input, 
                  int_channel_output=feat.int_channel_output, 
                  int_sec_sleep_dry=feat.int_sec_sleep_dry, 
                  int_sec_sleep_wet=feat.int_sec_sleep_wet)
