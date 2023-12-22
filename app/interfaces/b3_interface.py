from abc import ABC, abstractmethod


class B3Interface(ABC):
    @abstractmethod
    def read_data_from_b3(self, file_path):
        pass
