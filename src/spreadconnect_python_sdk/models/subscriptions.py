from typing import List, Optional, Literal
from pydantic import RootModel
from .common import CamelModel

EventType = Literal[
    "Shipment.sent",
    "Order.cancelled",
    "Order.processed",
    "Order.needs-action",
    "Article.added",
    "Article.updated",
    "Article.removed",
]


class Subscription(CamelModel):
    id: Optional[str] = None
    event_type: EventType
    url: str
    secret: Optional[str] = None


class GetSubscriptionsResponse(RootModel[List[Subscription]]):
    pass
