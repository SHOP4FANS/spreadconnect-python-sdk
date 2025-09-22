from typing import List, Optional
from pydantic import BaseModel

class ViewHotspot(BaseModel):
    name: Optional[str] = None

class ViewImage(BaseModel):
    appearance_id: str
    image: str

class View(BaseModel):
    name: Optional[str] = None
    id: Optional[str] = None
    hotspots: Optional[List[ViewHotspot]] = None
    images: Optional[List[ViewImage]] = None

class Views(BaseModel):
    views: Optional[List[View]] = None

class GetProductTypeViewsResponse(Views):
    pass

class GetProductTypeDesignHotspotsResponse(BaseModel):
    hotspots: Optional[List[dict]] = None
