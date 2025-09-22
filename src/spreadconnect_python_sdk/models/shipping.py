from typing import Optional, Literal
from pydantic import BaseModel
from .address import Address
from .price import Price, CustomerPrice

PreferredShippingType = Literal["STANDARD", "PREMIUM", "EXPRESS"]

class ShippingType(BaseModel):
    id: Optional[str] = None
    company: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None

class AvailableShippingType(ShippingType):
    price: Optional[Price] = None

class ShippingInfo(BaseModel):
    address: Optional[Address] = None
    from_address: Optional[Address] = None
    type: Optional[ShippingType] = None
    price: Optional[Price] = None
    customer_price: Optional[CustomerPrice] = None

class GetShippingTypesResponse(BaseModel):
    __root__: list[AvailableShippingType]
