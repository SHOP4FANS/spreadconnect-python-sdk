from typing import List, Optional
from .common import CamelModel


class CategoryNode(CamelModel):
    id: Optional[str] = None
    translation: Optional[str] = None
    children: Optional[List["CategoryNode"]] = None


class Feature(CamelModel):
    id: Optional[str] = None
    translation: Optional[str] = None


class BrandCategory(CamelModel):
    id: Optional[str] = None
    translation: Optional[str] = None


class Gender(CamelModel):
    id: Optional[str] = None
    translation: Optional[str] = None


class Categories(CamelModel):
    categories: Optional[List[CategoryNode]] = None
    features: Optional[List[Feature]] = None
    brands: Optional[List[BrandCategory]] = None
    genders: Optional[List[Gender]] = None


class GetProductTypeCategoriesResponse(Categories):
    pass
