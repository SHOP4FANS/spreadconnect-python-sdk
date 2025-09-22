from typing import List, Optional
from pydantic import BaseModel

class ArticleImage(BaseModel):
    id: Optional[int] = None
    product_id: Optional[int] = None
    appearance_id: Optional[int] = None
    appearance_name: Optional[str] = None
    perspective: Optional[str] = None
    image_url: Optional[str] = None

class ArticleConfiguration(BaseModel):
    image: dict
    view: str
    hotspot: Optional[str] = None

class ArticleVariant(BaseModel):
    id: Optional[int] = None
    product_type_id: Optional[int] = None
    product_type_name: Optional[str] = None
    product_id: Optional[int] = None
    appearance_id: Optional[int] = None
    appearance_name: Optional[str] = None
    appearance_color_value: Optional[str] = None
    size_id: Optional[int] = None
    size_name: Optional[str] = None
    sku: Optional[str] = None
    d2c_price: Optional[float] = None
    b2b_price: Optional[float] = None
    image_ids: Optional[List[int]] = None

class Article(BaseModel):
    id: Optional[int] = None
    title: Optional[str] = None
    description: Optional[str] = None
    variants: Optional[List[ArticleVariant]] = None
    images: Optional[List[ArticleImage]] = None

class ArticleCreation(BaseModel):
    title: str
    description: str
    variants: List[dict]
    configurations: List[ArticleConfiguration]
    external_id: Optional[str] = None

class GetArticlesParams(BaseModel):
    limit: Optional[int] = None
    offset: Optional[int] = None

class GetArticlesResponse(BaseModel):
    items: Optional[List[Article]] = None
    count: int
    limit: int
    offset: Optional[int] = None

class CreateArticleResponse(BaseModel):
    __root__: int

class GetSingleArticleResponse(Article):
    pass

class DeleteSingleArticleResponse(BaseModel):
    __root__: None
