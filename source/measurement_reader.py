import time

class MeasurementReader():
	def __init__(self, duration, number_of_measurements):
		self.duration = duration
		self.number_of_measurements = number_of_measurements
		self.sources = {}
		
	def start_to_measure(self):
		while True:
			self.get_one_series_of_measurements()

	def get_one_series_of_measurements(self):
		for i in xrange(self.number_of_measurements):
			time.sleep(1.0 * self.duration.total_seconds()/self.number_of_measurements)
			results_storage = {}
			self.get_measurements(results_storage)
			for device_unique_name in results_storage:
				print("Reading #{}: {}".format(i, self.sources[device_unique_name].get_formatted_measurement(results_storage[device_unique_name])))


	def get_measurements(self, results_storage=None):
		for source_unique_name in self.sources:
			self.sources[source_unique_name].get_measurement(results_storage)
	
	def add_source(self, source):
		self.sources[source.device_unique_name] = source

	def set_timeout(self, timeout):
		self.timeout = timeout
