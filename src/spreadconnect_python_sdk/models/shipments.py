from typing import List, Optional
from pydantic import RootModel
from .common import CamelModel


class TrackingInfo(CamelModel):
    code: Optional[str] = None
    url: Optional[str] = None


class Shipment(CamelModel):
    id: Optional[int] = None
    order_id: Optional[int] = None
    order_reference: Optional[int] = None
    external_order_reference: Optional[str] = None
    order_item_references: Optional[List[int]] = None
    external_order_item_references: Optional[List[str]] = None
    shipping: Optional[dict] = None
    tracking: Optional[List[TrackingInfo]] = None
    closed_date: Optional[str] = None
    sent_date: Optional[str] = None


class GetShipmentsResponse(RootModel[List[Shipment]]):
    pass
