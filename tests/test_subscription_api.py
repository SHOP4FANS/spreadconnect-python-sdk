import pytest
from unittest.mock import ANY
from spreadconnect_python_sdk.api.subscriptions import SubscriptionsApi
from spreadconnect_python_sdk.endpoints import (
    SUBSCRIPTIONS_PATH,
    ORDER_SIMULATE_CANCELLED_EVENT_PATH,
    ORDER_SIMULATE_PROCESSED_EVENT_PATH,
    ORDER_SIMULATE_SHIPMENT_SENT_EVENT_PATH,
)
from tests.__mocks__.subscriptions import (
    CreateSubscriptionPropsMock,
    GetSubscriptionsResponseMock,
)


def test_create_subscription(mocker):
    mock_client = mocker.Mock()
    mock_client.request.return_value = None
    api = SubscriptionsApi(mock_client)

    result = api.create(CreateSubscriptionPropsMock)

    assert result is None
    mock_client.request.assert_called_once_with(
        "POST",
        SUBSCRIPTIONS_PATH,
        response_model=None,
        json=ANY,
    )


def test_list_subscriptions(mocker):
    mock_client = mocker.Mock()
    mock_client.request.return_value = GetSubscriptionsResponseMock
    api = SubscriptionsApi(mock_client)

    res = api.list()
    assert res == GetSubscriptionsResponseMock

    mock_client.request.assert_called_once_with(
        "GET",
        SUBSCRIPTIONS_PATH,
        response_model=ANY,
    )


def test_delete_subscription(mocker):
    mock_client = mocker.Mock()
    mock_client.request.return_value = None
    api = SubscriptionsApi(mock_client)

    res = api.delete("10")
    assert res is None

    mock_client.request.assert_called_once_with(
        "DELETE",
        f"{SUBSCRIPTIONS_PATH}/10",
        response_model=None,
    )


def test_simulate_order_cancelled(mocker):
    mock_client = mocker.Mock()
    mock_client.request.return_value = None
    api = SubscriptionsApi(mock_client)

    res = api.simulate_order_cancelled("10")
    assert res is None

    mock_client.request.assert_called_once_with(
        "POST",
        ORDER_SIMULATE_CANCELLED_EVENT_PATH.replace("{orderId}", "10"),
        response_model=None,
    )


def test_simulate_order_processed(mocker):
    mock_client = mocker.Mock()
    mock_client.request.return_value = None
    api = SubscriptionsApi(mock_client)

    res = api.simulate_order_processed("10")
    assert res is None

    mock_client.request.assert_called_once_with(
        "POST",
        ORDER_SIMULATE_PROCESSED_EVENT_PATH.replace("{orderId}", "10"),
        response_model=None,
    )


def test_simulate_shipment_sent(mocker):
    mock_client = mocker.Mock()
    mock_client.request.return_value = None
    api = SubscriptionsApi(mock_client)

    res = api.simulate_shipment_sent("10")
    assert res is None

    mock_client.request.assert_called_once_with(
        "POST",
        ORDER_SIMULATE_SHIPMENT_SENT_EVENT_PATH.replace("{orderId}", "10"),
        response_model=None,
    )


def test_subscriptions_network_error(mocker):
    mock_client = mocker.Mock()
    mock_client.request.side_effect = Exception("Network Error")
    api = SubscriptionsApi(mock_client)

    with pytest.raises(Exception) as exc:
        api.list()

    assert "Network Error" in str(exc.value)
