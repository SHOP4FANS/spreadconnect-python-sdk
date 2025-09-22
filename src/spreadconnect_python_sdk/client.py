from spreadconnect_python_sdk.http.client import HttpClient
from spreadconnect_python_sdk.api.articles import ArticlesApi
from spreadconnect_python_sdk.api.orders import OrdersApi
from spreadconnect_python_sdk.api.subscriptions import SubscriptionsApi
from spreadconnect_python_sdk.api.product_types import ProductTypesApi
from spreadconnect_python_sdk.api.stocks import StocksApi
from spreadconnect_python_sdk.api.designs import DesignsApi


class Spreadconnect:
    def __init__(self, base_url: str, token: str) -> None:
        client = HttpClient(base_url, token)

        self.articles = ArticlesApi(client)
        self.orders = OrdersApi(client)
        self.subscriptions = SubscriptionsApi(client)
        self.product_types = ProductTypesApi(client)
        self.stocks = StocksApi(client)
        self.designs = DesignsApi(client)
