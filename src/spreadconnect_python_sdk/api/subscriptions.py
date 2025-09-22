from spreadconnect_python_sdk.http.client import HttpClient
from spreadconnect_python_sdk.endpoints import (
    SUBSCRIPTIONS_PATH,
    ORDER_SIMULATE_CANCELLED_EVENT_PATH,
    ORDER_SIMULATE_PROCESSED_EVENT_PATH,
    ORDER_SIMULATE_SHIPMENT_SENT_EVENT_PATH,
)
from spreadconnect_python_sdk.models.subscriptions import (
    Subscription,
    GetSubscriptionsResponse,
)


class SubscriptionsApi:
    """
    Provides access to the `/subscriptions` endpoints of the Spreadconnect API.
    """

    def __init__(self, client: HttpClient) -> None:
        """
        Initialize the Subscriptions API client.

        Parameters
        ----------
        client : HttpClient
            The shared HTTP client instance used for making requests.
        """
        self._client = client

    def create(self, subscription: Subscription) -> None:
        """
        Create a new subscription for specific event notifications.

        Sends a POST request to the `/subscriptions` endpoint.

        Parameters
        ----------
        subscription : Subscription
            The subscription data:
            - `event_type`: The type of event to subscribe to (required).
            - `url`: The URL to which notifications will be sent.
            - `secret`: Optional secret for verifying webhook payloads.

        Returns
        -------
        None
            Raises an error if creation fails.
        """
        self._client.request(
            "POST",
            SUBSCRIPTIONS_PATH,
            response_model=None,
            json=subscription.model_dump(exclude_none=True),
        )

    def list(self) -> GetSubscriptionsResponse:
        """
        Retrieve the list of active subscriptions.

        Sends a GET request to the `/subscriptions` endpoint.

        Returns
        -------
        GetSubscriptionsResponse
            A list of subscriptions currently active.
        """
        return self._client.request(
            "GET",
            SUBSCRIPTIONS_PATH,
            response_model=GetSubscriptionsResponse,
        )

    def delete(self, subscription_id: str) -> None:
        """
        Delete an existing subscription by its ID.

        Sends a DELETE request to `/subscriptions/{subscriptionId}`.

        Parameters
        ----------
        subscription_id : str
            The ID of the subscription to delete.

        Returns
        -------
        None
            Raises an error if deletion fails.
        """
        self._client.request(
            "DELETE",
            f"{SUBSCRIPTIONS_PATH}/{subscription_id}",
            response_model=None,
        )

    def simulate_order_cancelled(self, order_id: str) -> None:
        """
        Simulate the `Order.cancelled` webhook event for a given order.

        Sends a POST request to `/orders/{orderId}/simulate/order-cancelled`.

        Parameters
        ----------
        order_id : str
            The ID of the order.

        Returns
        -------
        None
            Raises an error if simulation fails.
        """
        self._client.request(
            "POST",
            ORDER_SIMULATE_CANCELLED_EVENT_PATH.replace("{orderId}", order_id),
            response_model=None,
        )

    def simulate_order_processed(self, order_id: str) -> None:
        """
        Simulate the `Order.processed` webhook event for a given order.

        Sends a POST request to `/orders/{orderId}/simulate/order-processed`.

        Parameters
        ----------
        order_id : str
            The ID of the order.

        Returns
        -------
        None
            Raises an error if simulation fails.
        """
        self._client.request(
            "POST",
            ORDER_SIMULATE_PROCESSED_EVENT_PATH.replace("{orderId}", order_id),
            response_model=None,
        )

    def simulate_shipment_sent(self, order_id: str) -> None:
        """
        Simulate the `Shipment.sent` webhook event for a given order.

        Sends a POST request to `/orders/{orderId}/simulate/shipment-sent`.

        Parameters
        ----------
        order_id : str
            The ID of the order.

        Returns
        -------
        None
            Raises an error if simulation fails.
        """
        self._client.request(
            "POST",
            ORDER_SIMULATE_SHIPMENT_SENT_EVENT_PATH.replace("{orderId}", order_id),
            response_model=None,
        )
