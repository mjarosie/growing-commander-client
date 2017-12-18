import time

class MeasurementReader():
	def __init__(self, duration, number_of_measurements):
		self.duration = duration
		self.number_of_measurements = number_of_measurements
		self.sources = {}
		
	def start_readings(self):
		while True:
			time.sleep(1.0 * self.duration/self.number_of_measurements)
			results_storage = {}
			get_measurements(results_storage)
			for device_unique_name in results:
				print(sources[device_unique_name].print_formatted_measurement(results[device_unique_name]))

	def get_measurements(self, results_storage=None):
		for source in self.sources:
			source.get_measurement(results_storage)
	
	def add_source(self, source):
		self.sources[source.device_unique_name] = source

	def set_timeout(self, timeout):
		self.timeout = timeout
