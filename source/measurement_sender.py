from abc import ABC, abstractmethod


class MeasurementSender(ABC):

    @abstractmethod
    def send(self, raw_data):
        raise NotImplementedError('Implement this!')
