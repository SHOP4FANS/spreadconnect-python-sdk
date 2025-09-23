from spreadconnect_python_sdk.client import Spreadconnect

def test_spreadconnect_initializes_all_apis(mocker):
    fake_client = object()

    mock_http = mocker.patch("spreadconnect_python_sdk.client.HttpClient", return_value=fake_client)

    api_classes = {
        "articles": mocker.patch("spreadconnect_python_sdk.client.ArticlesApi"),
        "orders": mocker.patch("spreadconnect_python_sdk.client.OrdersApi"),
        "subscriptions": mocker.patch("spreadconnect_python_sdk.client.SubscriptionsApi"),
        "product_types": mocker.patch("spreadconnect_python_sdk.client.ProductTypesApi"),
        "stocks": mocker.patch("spreadconnect_python_sdk.client.StocksApi"),
        "designs": mocker.patch("spreadconnect_python_sdk.client.DesignsApi"),
    }

    base_url = "https://api.example.com"
    token = "tok"
    sdk = Spreadconnect(base_url, token)

    mock_http.assert_called_once_with(base_url, token)

    for attr, cls in api_classes.items():
        cls.assert_called_once_with(fake_client)
        assert hasattr(sdk, attr)
