import time
from datetime import datetime
import pandas as pd
from utils import get_formatted_measurement


class MeasurementReader():
	def __init__(self, idle_time, duration, number_of_measurements):
		self.idle_time = idle_time
		self.duration = duration
		self.number_of_measurements = number_of_measurements
		self.sources = {}
		
	def start_to_measure(self):
		i = 0
		while True:
			# Begin a series of measurements.
			results = self.get_one_series_of_measurements()
			
			agg = get_results_aggregate(results)
			
			for index, agg_row in agg.iterrows():
				# timestamp = agg_row['timestamp']
				# device_name = agg_row['device_name']
				# measurement_type = agg_row['measurement_type']
				# measurement_unit = agg_row['measurement_unit']
				# measurement_value = agg_row['measurement_value']
				
				print(get_formatted_measurement(agg_row))

			# Wait for 'idle_time' seconds between series of measurements.
			time.sleep(1.0 * self.idle_time.total_seconds())
			i += 1

	def get_one_series_of_measurements(self):
		''' Takes number of measurements within a given time range.
			Returns the structure which holds the time in which the
			first and last measurements were made, and results.
		'''
		results = pd.DataFrame()
		for i in xrange(self.number_of_measurements):
			timestamp = datetime.now()
			result = self.get_measurements()
			result['timestamp'] = timestamp
			results = results.append(result)
			
			time.sleep(1.0 * self.duration.total_seconds()/self.number_of_measurements)
		return results

	def get_measurements(self):
		res = pd.DataFrame()
		for source_unique_name in self.sources:
			res = res.append(self.sources[source_unique_name].get_measurement())
		return res
	
	def add_source(self, source):
		self.sources[source.device_unique_name] = source

	def set_timeout(self, timeout):
		self.timeout = timeout

def get_results_aggregate(results_df):
	# Obtain the mean measurement value per device per measurement type.
	mean_measurement_values = results_df.groupby(['device_name', 'measurement_type', 'measurement_unit']).mean().reset_index()
	
	# Obtain the mean timestamp from the whole measurement group
	# (we want to return a mean measurement instead of multiple ones).
	first_timestamp = results_df.iloc[0]['timestamp']
	last_timestamp = results_df.iloc[-1]['timestamp']
	mean_timestamp = first_timestamp + (last_timestamp - first_timestamp)/2.0

	mean_measurement_values['timestamp'] = mean_timestamp
	
	return mean_measurement_values
			
