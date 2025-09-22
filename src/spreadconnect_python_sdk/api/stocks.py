from typing import Optional
from spreadconnect_python_sdk.http.client import HttpClient
from spreadconnect_python_sdk.endpoints import STOCKS_PATH
from spreadconnect_python_sdk.models.stocks import (
    GetStocksResponse,
    GetStockByProductTypeResponse,
    GetStockResponse,
)

class StocksApi:
    """
    Provides access to the `/stock` endpoints of the Spreadconnect API.
    """

    def __init__(self, client: HttpClient) -> None:
        """
        Initialize the Stocks API client.

        Parameters
        ----------
        client : HttpClient
            The shared HTTP client instance used for making requests.
        """
        self._client = client

    def list(self, limit: Optional[int] = None, offset: Optional[int] = None) -> GetStocksResponse:
        """
        Retrieve the available stock for all variants in the point of sale.

        Sends a GET request to the `/stock` endpoint.
        The result is a map of SKU identifiers associated with their stock amount.

        Parameters
        ----------
        limit : int, optional
            Maximum number of results to return.
        offset : int, optional
            The offset to start retrieving records from.

        Returns
        -------
        GetStocksResponse
            Stock information for all variants, paginated.
        """
        query = {}
        if limit is not None:
            query["limit"] = limit
        if offset is not None:
            query["offset"] = offset

        return self._client.request(
            "GET",
            STOCKS_PATH,
            response_model=GetStocksResponse,
            query_params=query or None,
        )

    def get(self, sku: str) -> GetStockResponse:
        """
        Retrieve the available stock for a specific variant by its SKU.

        Sends a GET request to the `/stock/{sku}` endpoint.

        Parameters
        ----------
        sku : str
            The Stock Keeping Unit (SKU) identifier of the variant.

        Returns
        -------
        GetStockResponse
            The stock amount for the specified variant.
        """
        return self._client.request(
            "GET",
            f"{STOCKS_PATH}/{sku}",
            response_model=GetStockResponse,
        )

    def get_by_product_type(self, product_type_id: str) -> GetStockByProductTypeResponse:
        """
        Retrieve the available stock for a specific product type with all its variants.

        Sends a GET request to the `/stock/productType/{productTypeId}` endpoint.

        Parameters
        ----------
        product_type_id : str
            The ID of the product type to retrieve stock for.

        Returns
        -------
        GetStockByProductTypeResponse
            Stock information grouped by variants (appearance + size).
        """
        return self._client.request(
            "GET",
            f"{STOCKS_PATH}/productType/{product_type_id}",
            response_model=GetStockByProductTypeResponse,
        )
