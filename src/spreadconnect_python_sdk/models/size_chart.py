from typing import List, Optional
from pydantic import BaseModel

class Measurement(BaseModel):
    name: Optional[str] = None
    value_mm: Optional[int] = None
    value_inch: Optional[int] = None

class SizeInfo(BaseModel):
    size_id: Optional[str] = None
    name: Optional[str] = None
    measurements: Optional[List[Measurement]] = None

class SizeChart(BaseModel):
    size_image_url: Optional[str] = None
    sizes: Optional[List[SizeInfo]] = None

class GetSingleSizeChartResponse(SizeChart):
    pass
