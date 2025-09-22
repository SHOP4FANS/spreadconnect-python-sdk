from typing import List, Optional
from .common import CamelModel


class ViewHotspot(CamelModel):
    name: Optional[str] = None


class ViewImage(CamelModel):
    appearance_id: str
    image: str


class View(CamelModel):
    name: Optional[str] = None
    id: Optional[str] = None
    hotspots: Optional[List[ViewHotspot]] = None
    images: Optional[List[ViewImage]] = None


class Views(CamelModel):
    views: Optional[List[View]] = None


class GetProductTypeViewsResponse(Views):
    pass


class GetProductTypeDesignHotspotsResponse(CamelModel):
    hotspots: Optional[List[dict]] = None
