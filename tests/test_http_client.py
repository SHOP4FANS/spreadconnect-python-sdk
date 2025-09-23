import pytest
from unittest.mock import MagicMock
from spreadconnect_python_sdk.http.client import HttpClient
from spreadconnect_python_sdk.exceptions import SpreadconnectError, OrderError
from spreadconnect_python_sdk.models.errors import ErrorResponse
from pydantic import BaseModel


class DummyModel(BaseModel):
    foo: str


def make_response(status=200, json_data=None, text_data="{}", is_success=True):
    m = MagicMock()
    m.status_code = status
    m.is_success = is_success
    m.text = text_data
    if json_data is not None:
        m.json.return_value = json_data
    else:
        m.json.side_effect = Exception("no json")
    return m


def test_builds_correct_url_and_headers(mocker):
    mocked_httpx = mocker.patch("httpx.Client")
    fake = MagicMock()
    mocked_httpx.return_value = fake
    fake.request.return_value = make_response(json_data={"foo": "bar"})
    client = HttpClient("https://api.example.com", "test-token")

    res = client.request("GET", "/test", DummyModel)

    fake.request.assert_called_once_with(
        method="GET",
        url="https://api.example.com/test",
        headers={"X-SPOD-ACCESS-TOKEN": "test-token"},
        params=None,
        json=None,
        data=None,
        files=None,
    )
    assert isinstance(res, DummyModel)
    assert res.foo == "bar"


def test_handles_query_params(mocker):
    mocked_httpx = mocker.patch("httpx.Client")
    fake = MagicMock()
    mocked_httpx.return_value = fake
    fake.request.return_value = make_response(json_data={"foo": "bar"})
    client = HttpClient("https://api.example.com", "tok")

    client.request("GET", "/test", DummyModel, query_params={"a": 1})
    kwargs = fake.request.call_args.kwargs
    assert kwargs["params"] == {"a": 1}


def test_raises_spreadconnect_error_on_failure(mocker):
    mocked_httpx = mocker.patch("httpx.Client")
    fake = MagicMock()
    mocked_httpx.return_value = fake
    fake.request.return_value = make_response(status=500, text_data="boom", is_success=False)
    client = HttpClient("base", "tok")

    with pytest.raises(SpreadconnectError) as exc:
        client.request("GET", "/fail")

    assert exc.value.status_code == 500


def test_raises_ordererror_on_confirm_cancel_failure(mocker):
    mocked_httpx = mocker.patch("httpx.Client")
    fake = MagicMock()
    mocked_httpx.return_value = fake
    fake.request.return_value = make_response(status=422, json_data={"reason": "oops"}, is_success=False)
    client = HttpClient("base", "tok")

    with pytest.raises(OrderError) as exc:
        client.request("POST", "/order/10/confirm")
    assert isinstance(exc.value.error, ErrorResponse)
    assert exc.value.status_code == 422


def test_returns_raw_json_if_no_model(mocker):
    mocked_httpx = mocker.patch("httpx.Client")
    fake = MagicMock()
    mocked_httpx.return_value = fake
    fake.request.return_value = make_response(json_data={"foo": "bar"})
    client = HttpClient("base", "tok")

    result = client.request("GET", "/raw")
    assert result == {"foo": "bar"}


def test_handles_invalid_json_gracefully(mocker):
    mocked_httpx = mocker.patch("httpx.Client")
    fake = MagicMock()
    mocked_httpx.return_value = fake
    fake.request.return_value = make_response()
    client = HttpClient("base", "tok")

    result = client.request("GET", "/invalid", DummyModel)
    assert result is None
