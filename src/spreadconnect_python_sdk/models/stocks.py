from typing import List, Optional, Dict
from pydantic import BaseModel, RootModel

class GetStocksResponse(BaseModel):
    items: Optional[Dict[str, int]] = None
    count: int
    limit: int
    offset: Optional[int] = None

class StockVariantByProductType(BaseModel):
    appearance_id: str
    size_id: str
    stock: int

class GetStockByProductTypeResponse(BaseModel):
    variants: Optional[List[StockVariantByProductType]] = None

class GetStockResponse(RootModel[int]):
    pass
