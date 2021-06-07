# functions
import datetime
import RPi.GPIO as GPIO
import time

# define class
class Interval_Watering:
	# initialize
	def __init__(self):
		pass
	# prepare board
	def prepare_board(self):
		# pin numbering using board
		GPIO.setmode(GPIO.BOARD)
		# disable warnings
		GPIO.setwarnings(False)
		return self
	# prepare inputs and outputs
	def prepare_io(self, int_channel_input=40, int_channel_output=15):
		# prepare board
		self.prepare_board()
		# configure a channel as an input (i.e., soil moisture sensor)
		GPIO.setup(int_channel_input, GPIO.IN)
		# configure a channel as an output
		GPIO.setup(int_channel_output, GPIO.OUT)
		return self
	# watering
	def watering(self, int_channel_input=40, int_channel_output=15, int_sec_sleep_dry=1, int_sec_sleep_wet=10, str_filename='dict_log.txt'):
		# prepare io
		self.prepare_io(int_channel_input=int_channel_input, 
						int_channel_output=int_channel_output)
		# instantiate empty dictionary
		self.dict_log = {}
		# begin while loop
		while True:
			# get initial value (1 == dry)
			int_moisture_level = GPIO.input(int_channel_input)
			# log it
			self.dict_log[datetime.datetime.now()] = int_moisture_level
			# write log
			with open(str_filename,'w') as data: 
 				data.write(str(self.dict_log))
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
					# log it
					self.dict_log[datetime.datetime.now()] = int_moisture_level
					# write log
					with open(str_filename,'w') as data: 
 						data.write(str(self.dict_log))
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
		return self