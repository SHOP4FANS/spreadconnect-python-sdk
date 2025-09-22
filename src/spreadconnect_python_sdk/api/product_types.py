from typing import Dict, Any
from spreadconnect_python_sdk.http.client import HttpClient
from spreadconnect_python_sdk.endpoints import PRODUCT_TYPES_PATH
from spreadconnect_python_sdk.models.products import (
    GetProductTypesResponse,
    GetSingleProductTypesResponse,
)
from spreadconnect_python_sdk.models.size_chart import GetSingleSizeChartResponse
from spreadconnect_python_sdk.models.categories import GetProductTypeCategoriesResponse
from spreadconnect_python_sdk.models.views import (
    GetProductTypeViewsResponse,
    GetProductTypeDesignHotspotsResponse,
)
from spreadconnect_python_sdk.models.preview import GetProductTypePreviewsResponse


class ProductTypesApi:
    """
    Provides access to the `/productTypes` endpoints of the Spreadconnect API.
    """

    def __init__(self, client: HttpClient) -> None:
        """
        Initialize the Product Types API client.

        Parameters
        ----------
        client : HttpClient
            The shared HTTP client instance used for making requests.
        """
        self._client = client

    def list(self) -> GetProductTypesResponse:
        """
        Retrieve all available product types.

        Sends a GET request to the `/productTypes` endpoint.

        Returns
        -------
        GetProductTypesResponse
            Information about all product types available for creating articles.
        """
        return self._client.request(
            "GET", PRODUCT_TYPES_PATH, response_model=GetProductTypesResponse
        )

    def get(self, product_type_id: str) -> GetSingleProductTypesResponse:
        """
        Retrieve detailed information about a specific product type.

        Sends a GET request to the `/productTypes/{productTypeId}` endpoint.

        Parameters
        ----------
        product_type_id : str
            The ID of the product type to retrieve.

        Returns
        -------
        GetSingleProductTypesResponse
            Detailed product type information.
        """
        return self._client.request(
            "GET",
            f"{PRODUCT_TYPES_PATH}/{product_type_id}",
            response_model=GetSingleProductTypesResponse,
        )

    def get_size_chart(self, product_type_id: str) -> GetSingleSizeChartResponse:
        """
        Retrieve the size chart for a specific product type.

        Sends a GET request to `/productTypes/{productTypeId}/size-chart`.

        Parameters
        ----------
        product_type_id : str
            The ID of the product type.

        Returns
        -------
        GetSingleSizeChartResponse
            The size chart information (image and measurements per size).
        """
        return self._client.request(
            "GET",
            f"{PRODUCT_TYPES_PATH}/{product_type_id}/size-chart",
            response_model=GetSingleSizeChartResponse,
        )

    def get_category_tree(self) -> GetProductTypeCategoriesResponse:
        """
        Retrieve the entire category tree of product types.

        Sends a GET request to `/productTypes/categories`.

        Returns
        -------
        GetProductTypeCategoriesResponse
            The full category tree including categories, features, brands and genders.
        """
        return self._client.request(
            "GET",
            f"{PRODUCT_TYPES_PATH}/categories",
            response_model=GetProductTypeCategoriesResponse,
        )

    def get_categories_by_product_type(
        self, product_type_id: str
    ) -> GetProductTypeCategoriesResponse:
        """
        Retrieve categories assigned to a specific product type.

        Sends a GET request to `/productTypes/{productTypeId}/categories`.

        Parameters
        ----------
        product_type_id : str
            The ID of the product type.

        Returns
        -------
        GetProductTypeCategoriesResponse
            Category information for the given product type.
        """
        return self._client.request(
            "GET",
            f"{PRODUCT_TYPES_PATH}/{product_type_id}/categories",
            response_model=GetProductTypeCategoriesResponse,
        )

    def get_views(self, product_type_id: str) -> GetProductTypeViewsResponse:
        """
        Retrieve all views (front, back, etc.), including hotspots and images, for a product type.

        Sends a GET request to `/productTypes/{productTypeId}/views`.

        Parameters
        ----------
        product_type_id : str
            The ID of the product type.

        Returns
        -------
        GetProductTypeViewsResponse
            Views including hotspots and images.
        """
        return self._client.request(
            "GET",
            f"{PRODUCT_TYPES_PATH}/{product_type_id}/views",
            response_model=GetProductTypeViewsResponse,
        )

    def get_design_hotspots(
        self, product_type_id: str, design_id: str
    ) -> GetProductTypeDesignHotspotsResponse:
        """
        Retrieve available design hotspots for a product type and design.

        Sends a GET request to `/productTypes/{productTypeId}/hotspots/design/{designId}`.

        Parameters
        ----------
        product_type_id : str
            The product type ID.
        design_id : str
            The design ID to check against.

        Returns
        -------
        GetProductTypeDesignHotspotsResponse
            The list of available hotspots for the given design.
        """
        return self._client.request(
            "GET",
            f"{PRODUCT_TYPES_PATH}/{product_type_id}/hotspots/design/{design_id}",
            response_model=GetProductTypeDesignHotspotsResponse,
        )

    def get_previews(
        self,
        product_type_id: str,
        body: Dict[str, Any],
    ) -> GetProductTypePreviewsResponse:
        """
        Retrieve preview images for a product type given hotspot-design configurations.

        Sends a POST request to `/productTypes/{productTypeId}/previews`.

        Parameters
        ----------
        product_type_id : str
            The ID of the product type.
        body : dict
            The preview request body, including configurations, appearanceId, width, height.

        Returns
        -------
        GetProductTypePreviewsResponse
            Preview images according to the given configuration.
        """
        return self._client.request(
            "POST",
            f"{PRODUCT_TYPES_PATH}/{product_type_id}/previews",
            response_model=GetProductTypePreviewsResponse,
            json=body,
        )
