import pytest
from unittest.mock import ANY
from spreadconnect_python_sdk.api.orders import OrdersApi
from spreadconnect_python_sdk.endpoints import ORDERS_PATH
from tests.__mocks__.orders import (
    CreateOrderMock,
    UpdateOrderMock,
    GetOrderMock,
    GetAvailableShippingTypesMock,
    GetShipmentsMock,
)


def test_get_single_order(mocker):
    mock_client = mocker.Mock()
    mock_client.request.return_value = GetOrderMock
    api = OrdersApi(mock_client)

    result = api.get("10")

    assert result == GetOrderMock
    mock_client.request.assert_called_once_with(
        "GET",
        f"{ORDERS_PATH}/10",
        response_model=ANY,
    )


def test_create_order(mocker):
    mock_client = mocker.Mock()
    mock_client.request.return_value = GetOrderMock
    api = OrdersApi(mock_client)

    result = api.create(CreateOrderMock)

    assert result == GetOrderMock
    mock_client.request.assert_called_once_with(
        "POST",
        ORDERS_PATH,
        response_model=ANY,
        json=ANY,
    )


def test_update_order(mocker):
    mock_client = mocker.Mock()
    mock_client.request.return_value = GetOrderMock
    api = OrdersApi(mock_client)

    result = api.update("10", UpdateOrderMock)

    assert result == GetOrderMock
    mock_client.request.assert_called_once_with(
        "PUT",
        f"{ORDERS_PATH}/10",
        response_model=ANY,
        json=ANY,
    )


def test_confirm_order(mocker):
    mock_client = mocker.Mock()
    mock_client.request.return_value = None
    api = OrdersApi(mock_client)

    result = api.confirm("10")

    assert result is None
    mock_client.request.assert_called_once_with(
        "POST",
        f"{ORDERS_PATH}/10/confirm",
        response_model=None,
    )


def test_cancel_order(mocker):
    mock_client = mocker.Mock()
    mock_client.request.return_value = None
    api = OrdersApi(mock_client)

    result = api.cancel("10")

    assert result is None
    mock_client.request.assert_called_once_with(
        "POST",
        f"{ORDERS_PATH}/10/cancel",
        response_model=None,
    )


def test_set_shipping_type(mocker):
    mock_client = mocker.Mock()
    mock_client.request.return_value = None
    api = OrdersApi(mock_client)

    result = api.set_shipping_type("10", "1")

    assert result is None
    mock_client.request.assert_called_once_with(
        "POST",
        f"{ORDERS_PATH}/10/shippingType",
        response_model=None,
        json={"id": "1"},
    )


def test_get_available_shipping_types(mocker):
    mock_client = mocker.Mock()
    mock_client.request.return_value = GetAvailableShippingTypesMock
    api = OrdersApi(mock_client)

    result = api.get_available_shipping_types("10")

    assert result == GetAvailableShippingTypesMock
    mock_client.request.assert_called_once_with(
        "GET",
        f"{ORDERS_PATH}/10/shippingTypes",
        response_model=ANY,
    )


def test_get_shipments(mocker):
    mock_client = mocker.Mock()
    mock_client.request.return_value = GetShipmentsMock
    api = OrdersApi(mock_client)

    result = api.get_shipments("10")

    assert result == GetShipmentsMock
    mock_client.request.assert_called_once_with(
        "GET",
        f"{ORDERS_PATH}/10/shipments",
        response_model=ANY,
    )


def test_order_network_error(mocker):
    mock_client = mocker.Mock()
    mock_client.request.side_effect = Exception("Network Error")
    api = OrdersApi(mock_client)

    with pytest.raises(Exception) as exc:
        api.get("10")

    assert "Network Error" in str(exc.value)
