from typing import Optional
from pydantic import BaseModel

class CustomerPrice(BaseModel):
    amount: float
    currency: Optional[str] = None

class Price(BaseModel):
    amount: float
    tax_rate: Optional[float] = None
    tax_amount: Optional[float] = None
    currency: Optional[str] = None
