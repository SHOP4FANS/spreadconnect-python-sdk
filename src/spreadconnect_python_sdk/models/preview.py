from typing import List, Optional
from pydantic import BaseModel

class PreviewImage(BaseModel):
    url: Optional[str] = None
    view_id: Optional[str] = None
    view_name: Optional[str] = None

class Preview(BaseModel):
    images: Optional[List[PreviewImage]] = None

class GetProductTypePreviewsResponse(Preview):
    pass
