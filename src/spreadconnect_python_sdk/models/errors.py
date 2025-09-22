from typing import Optional
from .common import CamelModel


class ErrorResponse(CamelModel):
    order_id: Optional[int] = None
    reason: Optional[str] = None
