from typing import Optional
from pydantic import BaseModel

class AuthResponse(BaseModel):
    merchant_id: Optional[int] = None
    point_of_sale_id: Optional[int] = None
    point_of_sale_name: Optional[str] = None
    point_of_sale_type: Optional[str] = None
