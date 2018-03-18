from abc import ABC, abstractmethod


class MeasurementSource(ABC):
    def __init__(self, device_unique_name):
        self.device_unique_name = device_unique_name
        self.measurement_types = []
        self.measurement_units = []
        self.gpio_pin = -1

    @abstractmethod
    def get_measurement(self, results_storage=None):
        raise NotImplementedError('Implement this!')
