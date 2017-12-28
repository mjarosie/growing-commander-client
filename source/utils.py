

def get_formatted_measurement(reading):
	ret_val = "{:%d %h %Y, %H:%M:%S} - {}: {}={:0.1f}{}"
	return ret_val.format(
						reading['timestamp'],
						reading['device_name'],
						
						reading['measurement_type'],
						reading['measurement_value'],
						reading['measurement_unit']
					)
