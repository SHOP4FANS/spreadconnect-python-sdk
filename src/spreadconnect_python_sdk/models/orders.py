from typing import List, Optional, Literal
from pydantic import BaseModel
from .address import Address
from .price import Price, CustomerPrice
from .articles import ArticleConfiguration
from .shipping import ShippingInfo

OrderState = Literal["NEW", "CONFIRMED", "PROCESSED", "CANCELLED"]
OrderItemState = Literal["NEW", "CHECKED", "CANCELLED", "PRODUCTION_ISSUE", "IN_PRODUCTION", "SENT"]
TaxType = Literal["SALESTAX", "VAT", "NOT_TAXABLE"]
CustomerTaxType = Literal["SALESTAX", "VAT", "NOT_TAXABLE"]

class GetOrderItem(BaseModel):
    order_item_reference: Optional[int] = None
    external_order_item_reference: Optional[str] = None
    state: Optional[OrderItemState] = None
    sku: Optional[str] = None
    quantity: int
    price: Optional[Price] = None
    customer_price: Optional[CustomerPrice] = None

class CreateOrderItem(BaseModel):
    sku: str
    quantity: int
    external_order_item_reference: Optional[str] = None
    customer_price: CustomerPrice

class QuantityItem(BaseModel):
    quantity: Optional[int] = None
    size_id: Optional[int] = None
    appearance_id: Optional[dict] = None

class OneTimeItem(BaseModel):
    quantity_items: Optional[List[QuantityItem]] = None
    configurations: Optional[List[ArticleConfiguration]] = None
    product_type_id: Optional[int] = None
    external_order_item_reference: Optional[str] = None
    customer_price_per_item: Optional[dict] = None

class Order(BaseModel):
    id: Optional[int] = None
    order_reference: Optional[int] = None
    external_order_reference: Optional[str] = None
    external_order_name: Optional[str] = None
    state: Optional[OrderState] = None
    order_items: Optional[List[GetOrderItem]] = None
    shipping: Optional[ShippingInfo] = None
    billing_address: Optional[Address] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    price: Optional[Price] = None
    tax_type: Optional[TaxType] = None
    customer_tax_type: Optional[CustomerTaxType] = None

class CreateOrder(BaseModel):
    order_items: List[CreateOrderItem]
    one_time_items: Optional[List[OneTimeItem]] = None
    shipping: dict
    billing_address: Optional[Address] = None
    phone: str
    email: str
    external_order_reference: str
    external_order_name: Optional[str] = None
    state: Optional[str] = None
    customer_tax_type: Optional[CustomerTaxType] = None
    origin: Optional[str] = None

class UpdateOrder(CreateOrder):
    pass

class CreateOrderResponse(Order):
    pass

class UpdateOrderResponse(Order):
    pass

class GetSingleOrderResponse(Order):
    pass
