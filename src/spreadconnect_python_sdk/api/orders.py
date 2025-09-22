from spreadconnect_python_sdk.http.client import HttpClient
from spreadconnect_python_sdk.endpoints import ORDERS_PATH
from spreadconnect_python_sdk.models.orders import (
    CreateOrder,
    UpdateOrder,
    CreateOrderResponse,
    UpdateOrderResponse,
    GetSingleOrderResponse,
)
from spreadconnect_python_sdk.models.shipping import GetShippingTypesResponse
from spreadconnect_python_sdk.models.shipments import GetShipmentsResponse


class OrdersApi:
    """
    Provides access to the `/orders` endpoints of the Spreadconnect API.
    """

    def __init__(self, client: HttpClient) -> None:
        """
        Initialize the Orders API client.

        Parameters
        ----------
        client : HttpClient
            The shared HTTP client instance used for making requests.
        """
        self._client = client

    def create(self, props: CreateOrder) -> CreateOrderResponse:
        """
        Create a new order.

        Sends a POST request to the `/orders` endpoint with the order details.
        You can choose to set the shipping type and confirm the order in one request,
        or create the order first and set these properties later.

        Parameters
        ----------
        props : CreateOrder
            The order data to create.

        Returns
        -------
        CreateOrderResponse
            Details of the created order.
        """
        return self._client.request(
            "POST",
            ORDERS_PATH,
            response_model=CreateOrderResponse,
            json=props.model_dump(exclude_none=True),
        )

    def update(self, order_id: str, props: UpdateOrder) -> UpdateOrderResponse:
        """
        Update an existing order.

        Sends a PUT request to the `/orders/{orderId}` endpoint with updated details.

        Parameters
        ----------
        order_id : str
            ID of the order to update.
        props : UpdateOrder
            The new order data.

        Returns
        -------
        UpdateOrderResponse
            Details of the updated order.
        """
        return self._client.request(
            "PUT",
            f"{ORDERS_PATH}/{order_id}",
            response_model=UpdateOrderResponse,
            json=props.model_dump(exclude_none=True),
        )

    def get(self, order_id: str) -> GetSingleOrderResponse:
        """
        Retrieve a specific order by its ID.

        Sends a GET request to the `/orders/{orderId}` endpoint.

        Parameters
        ----------
        order_id : str
            ID of the order to retrieve.

        Returns
        -------
        GetSingleOrderResponse
            The order details.
        """
        return self._client.request(
            "GET",
            f"{ORDERS_PATH}/{order_id}",
            response_model=GetSingleOrderResponse,
        )

    def confirm(self, order_id: str) -> None:
        """
        Confirm an order.

        Sends a POST request to `/orders/{orderId}/confirm`.
        To confirm an order, it is necessary to set a shipping type first.

        Parameters
        ----------
        order_id : str
            ID of the order to confirm.

        Returns
        -------
        None
            Raises `OrderError` if confirmation fails.
        """
        self._client.request(
            "POST",
            f"{ORDERS_PATH}/{order_id}/confirm",
            response_model=None,
        )

    def cancel(self, order_id: str) -> None:
        """
        Cancel an order.

        Sends a POST request to `/orders/{orderId}/cancel`.
        It is not possible to cancel orders that have already been sent
        or are already in production.

        Parameters
        ----------
        order_id : str
            ID of the order to cancel.

        Returns
        -------
        None
            Raises `OrderError` if cancellation fails.
        """
        self._client.request(
            "POST",
            f"{ORDERS_PATH}/{order_id}/cancel",
            response_model=None,
        )

    def get_available_shipping_types(
        self, order_id: str
    ) -> GetShippingTypesResponse:
        """
        Retrieve all available shipping types for a specific order.

        Sends a GET request to `/orders/{orderId}/shippingTypes`.

        Parameters
        ----------
        order_id : str
            The ID of the order.

        Returns
        -------
        GetShippingTypesResponse
            List of available shipping types.
        """
        return self._client.request(
            "GET",
            f"{ORDERS_PATH}/{order_id}/shippingTypes",
            response_model=GetShippingTypesResponse,
        )

    def set_shipping_type(self, order_id: str, shipping_type_id: str) -> None:
        """
        Set the shipping type for an order.

        Sends a POST request to `/orders/{orderId}/shippingType`.

        Parameters
        ----------
        order_id : str
            The ID of the order.
        shipping_type_id : str
            The ID of the shipping type to set.

        Returns
        -------
        None
            Raises an error if the shipping type cannot be set.
        """
        self._client.request(
            "POST",
            f"{ORDERS_PATH}/{order_id}/shippingType",
            response_model=None,
            json={"id": shipping_type_id},
        )

    def get_shipments(self, order_id: str) -> GetShipmentsResponse:
        """
        Retrieve all shipments for a specific order.

        Sends a GET request to `/orders/{orderId}/shipments`.

        Parameters
        ----------
        order_id : str
            The ID of the order.

        Returns
        -------
        GetShipmentsResponse
            All shipments belonging to the order.
        """
        return self._client.request(
            "GET",
            f"{ORDERS_PATH}/{order_id}/shipments",
            response_model=GetShipmentsResponse,
        )
