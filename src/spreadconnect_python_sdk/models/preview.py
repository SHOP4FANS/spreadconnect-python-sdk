from typing import List, Optional
from .common import CamelModel


class PreviewImage(CamelModel):
    url: Optional[str] = None
    view_id: Optional[str] = None
    view_name: Optional[str] = None


class Preview(CamelModel):
    images: Optional[List[PreviewImage]] = None


class GetProductTypePreviewsResponse(Preview):
    pass
