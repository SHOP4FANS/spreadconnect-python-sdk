from typing import Optional, Literal, List
from pydantic import BaseModel, RootModel

EventType = Literal[
    "Shipment.sent",
    "Order.cancelled",
    "Order.processed",
    "Order.needs-action",
    "Article.added",
    "Article.updated",
    "Article.removed"
]

class Subscription(BaseModel):
    id: Optional[int] = None
    event_type: EventType
    url: str
    secret: Optional[str] = None

class GetSubscriptionsResponse(RootModel[List[Subscription]]):
    pass
