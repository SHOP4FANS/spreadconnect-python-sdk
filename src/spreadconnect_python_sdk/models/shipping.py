from typing import Optional, Literal, List
from pydantic import RootModel
from .common import CamelModel
from .address import Address
from .price import Price, CustomerPrice

PreferredShippingType = Literal["STANDARD", "PREMIUM", "EXPRESS"]


class ShippingType(CamelModel):
    id: Optional[str] = None
    company: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None


class AvailableShippingType(ShippingType):
    price: Optional[Price] = None


class ShippingInfo(CamelModel):
    address: Optional[Address] = None
    from_address: Optional[Address] = None
    type: Optional[ShippingType] = None
    price: Optional[Price] = None
    customer_price: Optional[CustomerPrice] = None


class GetShippingTypesResponse(RootModel[List[AvailableShippingType]]):
    pass
