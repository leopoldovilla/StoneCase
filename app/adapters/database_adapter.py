from app.domain.models import db, TradeDb
from app.interfaces.database_interface import DatabaseInterface


class DatabaseAdapter(DatabaseInterface):
    def save_trades(self, trades_data):
        trades = []
        for trade_data in trades_data:
            trades.append(TradeDb(**trade_data))
        db.session.bulk_save_objects(trades)
        db.session.commit()

    def get_trades(self, ticker=None, business_date=None):
        query = TradeDb.query
        if ticker:
            query = query.filter(TradeDb.ticker == ticker)
        if business_date:
            query = query.filter(TradeDb.business_date == business_date)
        return query.all()

    def delete_all_trades(self):
        db.session.query(TradeDb).delete()
