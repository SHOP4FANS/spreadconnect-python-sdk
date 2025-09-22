from typing import Optional
from pydantic import BaseModel

class ErrorResponse(BaseModel):
    order_id: Optional[int] = None
    reason: Optional[str] = None
