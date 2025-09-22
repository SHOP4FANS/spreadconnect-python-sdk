from typing import Optional
from .common import CamelModel


class CustomerPrice(CamelModel):
    amount: float
    currency: Optional[str] = None


class Price(CamelModel):
    amount: float
    tax_rate: Optional[float] = None
    tax_amount: Optional[float] = None
    currency: Optional[str] = None
