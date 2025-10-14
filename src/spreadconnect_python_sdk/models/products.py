from typing import List, Optional, Literal

from pydantic import RootModel
from .common import CamelModel

ProductView = Literal["FRONT", "BACK", "LEFT", "RIGHT", "HOOD_LEFT", "HOOD_RIGHT"]


class ProductSize(CamelModel):
    id: Optional[str] = None
    name: Optional[str] = None


class ProductAppearance(CamelModel):
    id: Optional[str] = None
    name: Optional[str] = None


class ProductTypes(CamelModel):
    id: Optional[str] = None
    customer_name: Optional[str] = None
    customer_description: Optional[str] = None
    merchant_name: Optional[str] = None
    merchant_description: Optional[str] = None
    sizes: Optional[List[ProductSize]] = None
    brand: Optional[str] = None
    appearances: Optional[List[ProductAppearance]] = None
    views: Optional[List[ProductView]] = None
    price: Optional[float] = None
    currency: Optional[str] = None


class GetProductTypesResponse(RootModel[list[ProductTypes]]):
    pass


class GetSingleProductTypesResponse(ProductTypes):
    pass
