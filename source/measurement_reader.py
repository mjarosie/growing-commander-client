class MeasurementReader():
	def __init__(self, duration, number_of_measurements):
		self.duration = duration
		self.number_of_measurements = number_of_measurements
		self.sources = []

	def measure(self):
		for source in self.sources:
			source.get_reading()
	
	def add_source(self, source):
		self.sources.append(source)

	def set_timeout(self, timeout):
		self.timeout = timeout
