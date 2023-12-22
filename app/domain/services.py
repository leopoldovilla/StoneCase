import jsonpickle

from app.interfaces.b3_interface import B3Interface
from app.interfaces.database_interface import DatabaseInterface


class TradeService:
    def __init__(
        self,
        database_adapter: DatabaseInterface,
        b3_adapter: B3Interface,
    ):
        self.database_adapter = database_adapter
        self.b3_adapter = b3_adapter

    def process_b3_data(self, file_path: str):
        self.database_adapter.delete_all_trades()
        b3_data = self.b3_adapter.read_data_from_b3(file_path)
        self.database_adapter.save_trades(b3_data)

    def get_aggregated_data(self, ticker: str, business_date: str = None):
        trades = self.database_adapter.get_trades(ticker, business_date)
        trades_response = []
        for trade in trades:
            trades_response.append({
                'ticker': trade.ticker,
                'business_date': trade.business_date.strftime("%Y-%m-%d"),
                'max_range_value': trade.max_range_value,
                'max_daily_volume': trade.max_daily_volume,
            })
        return jsonpickle.encode(trades_response)


