from typing import List, Optional
from pydantic import BaseModel

class CategoryNode(BaseModel):
    id: Optional[str] = None
    translation: Optional[str] = None
    children: Optional[List["CategoryNode"]] = None

class Feature(BaseModel):
    id: Optional[str] = None
    translation: Optional[str] = None

class BrandCategory(BaseModel):
    id: Optional[str] = None
    translation: Optional[str] = None

class Gender(BaseModel):
    id: Optional[str] = None
    translation: Optional[str] = None

class Categories(BaseModel):
    categories: Optional[List[CategoryNode]] = None
    features: Optional[List[Feature]] = None
    brands: Optional[List[BrandCategory]] = None
    genders: Optional[List[Gender]] = None

class GetProductTypeCategoriesResponse(Categories):
    pass
