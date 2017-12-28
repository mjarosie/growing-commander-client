class MeasurementSource():
	def __init__(self, device_unique_name, unit=None):
		self.device_unique_name = device_unique_name
		self.measurement_types = []
		self.measurement_units = []
		self.gpio_pin = -1

	def get_measurement(self, results_storage=None):
		pass

