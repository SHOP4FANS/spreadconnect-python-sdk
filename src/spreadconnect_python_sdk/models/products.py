from typing import List, Optional, Literal
from pydantic import BaseModel

ProductView = Literal["FRONT", "BACK", "LEFT", "RIGHT", "HOOD_LEFT", "HOOD_RIGHT"]

class ProductSize(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None

class ProductAppearance(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None

class ProductTypes(BaseModel):
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

class GetProductTypesResponse(BaseModel):
    items: Optional[List[ProductTypes]] = None

class GetSingleProductTypesResponse(ProductTypes):
    pass
