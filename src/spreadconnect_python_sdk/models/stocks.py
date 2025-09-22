from typing import Optional, Dict, List
from pydantic import RootModel
from .common import CamelModel


class GetStocksResponse(CamelModel):
    items: Optional[Dict[str, int]] = None
    count: int
    limit: int
    offset: Optional[int] = None


class StockVariantByProductType(CamelModel):
    appearance_id: str
    size_id: str
    stock: int


class GetStockByProductTypeResponse(CamelModel):
    variants: Optional[List[StockVariantByProductType]] = None


class GetStockResponse(RootModel[int]):
    pass
