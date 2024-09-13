from app.stock_api import StockAPI

def test_get_stock_data():
    stock_api = StockAPI()
    data = stock_api.get_stock_data('TSLA')
    assert not data.empty