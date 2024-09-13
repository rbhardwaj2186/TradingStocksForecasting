from app.services import StockService

def test_get_forecast():
    service = StockService()
    forecast = service.get_forecast('TSLA', '2022-01-01', '2022-12-31', 'monthly')
    assert not forecast.empty

test_get_forecast()