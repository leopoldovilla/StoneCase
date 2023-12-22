from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class TradeDb(db.Model):
    __tablename__ = 'Negociacoes'
    id_trade = db.Column(db.Integer, primary_key=True, name='IdNegociacao', autoincrement=True)
    ticker = db.Column(db.String(255), name='CodigoInstrumento')
    business_date = db.Column(db.Date, name='DataNegocio')
    max_range_value = db.Column(db.Float, name='PrecoNegocio')
    max_daily_volume = db.Column(db.Integer, name='QuantidadeNegociada')

    def __init__(self, ticker, business_date, max_range_value, max_daily_volume):
        self.ticker = ticker
        self.business_date = business_date
        self.max_range_value = max_range_value
        self.max_daily_volume = max_daily_volume
