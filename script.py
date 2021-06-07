from functions import Interval_Watering
import features as feat

# initialize class
cls_interval_watering = Interval_Watering()

# water
cls_interval_watering.watering(int_channel_input=feat.int_channel_input, 
                               int_channel_output=feat.int_channel_output, 
                               int_sec_sleep_dry=feat.int_sec_sleep_dry, 
                               int_sec_sleep_wet=feat.int_sec_sleep_wet,
                               str_filename=feat.str_filename)
