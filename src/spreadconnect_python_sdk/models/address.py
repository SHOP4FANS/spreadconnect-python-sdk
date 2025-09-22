from typing import Optional
from .common import CamelModel


class Address(CamelModel):
    company: Optional[str] = None
    first_name: Optional[str] = None
    last_name: str
    street: str
    street_annex: Optional[str] = None
    city: str
    country: str
    state: Optional[str] = None
    zip_code: str
