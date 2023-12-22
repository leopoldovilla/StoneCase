import os
from datetime import (
    datetime,
)

from automapper import mapper
from flask import (
    Flask,
    request,
)

from app.adapters.b3_adapter import B3Adapter
from app.adapters.database_adapter import DatabaseAdapter
from app.domain.models import (
    db,
    TradeDb,
)
from app.domain.services import TradeService
from config import SQLALCHEMY_DATABASE_URI

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
db.init_app(app)

database_adapter = DatabaseAdapter()
b3_adapter = B3Adapter()
trade_service = TradeService(database_adapter, b3_adapter)

@app.route('/data', methods=['GET'])
def data():
    ticker = request.args.get('ticker')
    business_date = request.args.get('business_date')

    return trade_service.get_aggregated_data(ticker, business_date)


@app.route('/updateData', methods=['GET'])
def update_data():
    try:
        start_time = datetime.now()
        basedir = os.path.abspath(os.path.dirname(__file__))
        trade_service.process_b3_data(os.path.join(basedir, 'app', 'data'))
        return f"Dados atualizados com sucesso! Tempo para atualização: {datetime.now() - start_time}"
    except Exception as e:
        return "Erro ao atualizar dados: " + str(e)


if __name__ == '__main__':
    app.run(debug=True)
