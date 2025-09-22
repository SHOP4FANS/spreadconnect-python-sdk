from typing import Optional
from pydantic import BaseModel

class DesignUpload(BaseModel):
    file: Optional[bytes] = None
    url: Optional[str] = None

class DesignUploadResponse(BaseModel):
    design_id: str
