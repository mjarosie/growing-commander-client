from measurement_source import MeasurementSource
import Adafruit_DHT
import pandas as pd

class DhtThermometer(MeasurementSource):
	def __init__(self, device_unique_name, gpio_pin):
		self.device_unique_name = device_unique_name
		self.measurement_types = ['humidity', 'temperature']
		self.measurement_units = ['%', '*C']
		self.gpio_pin = gpio_pin
		self.sensor_type = Adafruit_DHT.AM2302
		
	def get_measurement(self, reading_function = None, *args, **kwargs):
		# Try to grab a sensor reading.  Use the read_retry method which will retry up
		# to 15 times to get a sensor reading (waiting 2 seconds between each retry).
		if reading_function is None:
			measurements = Adafruit_DHT.read_retry(self.sensor_type, self.gpio_pin)
		else:
			measurements = reading_function(*args, **kwargs)
		df = pd.DataFrame(columns=['device_name', 'measurement_type', 'measurement_unit', 'measurement_value'])
		df.loc[0] = [self.device_unique_name, self.measurement_types[0], self.measurement_units[0], measurements[0]]
		df.loc[1] = [self.device_unique_name, self.measurement_types[1], self.measurement_units[1], measurements[1]]
		return df
