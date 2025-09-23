from spreadconnect_python_sdk.models.subscriptions import Subscription, GetSubscriptionsResponse

CreateSubscriptionPropsMock = Subscription(
    event_type="Shipment.sent",
    url="https://example.com/webhook",
)

GetSubscriptionsResponseMock = GetSubscriptionsResponse(
    root=[
        Subscription(event_type="Shipment.sent", url="https://example.com/webhook")
    ]
)
