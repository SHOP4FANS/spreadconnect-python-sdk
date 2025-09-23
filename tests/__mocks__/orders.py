from spreadconnect_python_sdk.models.orders import (
    CreateOrder,
    CreateOrderItem,
    UpdateOrder,
    GetSingleOrderResponse,
)
from spreadconnect_python_sdk.models.price import CustomerPrice
from spreadconnect_python_sdk.models.shipping import GetShippingTypesResponse
from spreadconnect_python_sdk.models.shipments import GetShipmentsResponse

CreateOrderMock = CreateOrder(
    order_items=[
        CreateOrderItem(
            sku="SKU123",
            quantity=1,
            customer_price=CustomerPrice(amount=9.99, currency="EUR"),
        )
    ],
    shipping={
        "address": {
            "lastName": "Doe",
            "street": "Main St",
            "city": "Berlin",
            "country": "DE",
            "zipCode": "10115",
        },
        "customerPrice": {"amount": 4.99, "currency": "EUR"},
    },
    phone="123456789",
    email="test@example.com",
    external_order_reference="mock-order-123",
)

UpdateOrderMock = UpdateOrder(**CreateOrderMock.model_dump())

GetOrderMock = GetSingleOrderResponse(
    id=10,
    external_order_reference="mock-order-123",
    state="NEW",
    phone="123456789",
    email="test@example.com",
)

GetAvailableShippingTypesMock = GetShippingTypesResponse(
    root=[]
)

GetShipmentsMock = GetShipmentsResponse(root=[])
