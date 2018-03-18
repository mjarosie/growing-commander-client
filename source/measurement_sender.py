from abc import ABC, abstractmethod


class MeasurementSender(ABC):

    @abstractmethod
    def send(self, data):
        raise NotImplementedError('Implement this!')
