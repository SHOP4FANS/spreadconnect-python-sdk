from typing import List, Optional
from pydantic import RootModel
from .common import CamelModel


class ArticleImage(CamelModel):
    id: Optional[int] = None
    product_id: Optional[int] = None
    appearance_id: Optional[int] = None
    appearance_name: Optional[str] = None
    perspective: Optional[str] = None
    image_url: Optional[str] = None


class ArticleConfigurationImage(CamelModel):
    url: Optional[str] = None
    design_id: Optional[str] = None


class ArticleConfiguration(CamelModel):
    image: dict
    view: str
    hotspot: Optional[str] = None


class ArticleVariant(CamelModel):
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


class Article(CamelModel):
    id: Optional[int] = None
    title: Optional[str] = None
    description: Optional[str] = None
    variants: Optional[List[ArticleVariant]] = None
    images: Optional[List[ArticleImage]] = None


class ArticleCreationVariant(CamelModel):
    product_type_id: int
    appearance_id: int
    size_id: int
    d2c_price: Optional[float] = None
    external_id: Optional[str] = None


class ArticleCreation(CamelModel):
    title: str
    description: str
    variants: List[ArticleCreationVariant]
    configurations: List[ArticleConfiguration]
    external_id: Optional[str] = None


class GetArticlesParams(CamelModel):
    limit: Optional[int] = None
    offset: Optional[int] = None


class GetArticlesResponse(CamelModel):
    items: Optional[List[Article]] = None
    count: int
    limit: int
    offset: Optional[int] = None


class CreateArticleResponse(RootModel[int]):
    pass


class GetSingleArticleResponse(Article):
    pass


class DeleteSingleArticleResponse(RootModel[None]):
    pass
