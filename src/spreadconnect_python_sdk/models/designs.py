from typing import Optional
from .common import CamelModel


class DesignUpload(CamelModel):
    file: Optional[bytes] = None
    url: Optional[str] = None


class DesignUploadResponse(CamelModel):
    design_id: str
