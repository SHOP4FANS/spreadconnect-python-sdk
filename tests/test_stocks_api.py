import pytest
from unittest.mock import ANY
from spreadconnect_python_sdk.api.stocks import StocksApi
from spreadconnect_python_sdk.endpoints import STOCKS_PATH
from tests.__mocks__.stocks import (
    StocksResponseMock,
    StockResponseMock,
    GetStockByProductTypeResponseMock,
)


def test_list_stocks(mocker):
    mock_client = mocker.Mock()
    mock_client.request.return_value = StocksResponseMock
    api = StocksApi(mock_client)

    result = api.list(limit=0, offset=10)

    assert result == StocksResponseMock
    mock_client.request.assert_called_once_with(
        "GET",
        STOCKS_PATH,
        response_model=ANY,
        query_params={"limit": 0, "offset": 10},
    )


def test_get_single_stock(mocker):
    mock_client = mocker.Mock()
    mock_client.request.return_value = StockResponseMock
    api = StocksApi(mock_client)

    result = api.get("test")
    assert result == StockResponseMock

    mock_client.request.assert_called_once_with(
        "GET",
        f"{STOCKS_PATH}/test",
        response_model=ANY,
    )


def test_get_stock_by_product_type(mocker):
    mock_client = mocker.Mock()
    mock_client.request.return_value = GetStockByProductTypeResponseMock
    api = StocksApi(mock_client)

    result = api.get_by_product_type("10")
    assert result == GetStockByProductTypeResponseMock

    mock_client.request.assert_called_once_with(
        "GET",
        f"{STOCKS_PATH}/productType/10",
        response_model=ANY,
    )


def test_stock_network_error(mocker):
    mock_client = mocker.Mock()
    mock_client.request.side_effect = Exception("Network Error")
    api = StocksApi(mock_client)

    with pytest.raises(Exception) as exc:
        api.get("10")

    assert "Network Error" in str(exc.value)
