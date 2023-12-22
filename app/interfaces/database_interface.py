from abc import ABC, abstractmethod


class DatabaseInterface(ABC):
    @abstractmethod
    def save_trades(self, trade_data):
        pass

    @abstractmethod
    def get_trades(self, ticker, start_date=None):
        pass

    @abstractmethod
    def delete_all_trades(self):
        pass
