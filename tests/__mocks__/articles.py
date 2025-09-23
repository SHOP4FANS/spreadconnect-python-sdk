from spreadconnect_python_sdk.models.articles import ArticleCreation, ArticleConfiguration, ArticleCreationVariant

GetSingleArticleMock = {
    "title": "Test article",
    "description": "A test description",
}

ArticleCreationMock = ArticleCreation(
    title="Test",
    description="test",
    variants=[ArticleCreationVariant(product_type_id=10, appearance_id=1, size_id=1)],
    configurations=[ArticleConfiguration(image={"url": "image"}, view="FRONT")],
)

GetSingleArticleResponseMock = {
    "status": 200,
    "data": GetSingleArticleMock,
}

GetArticlesResponseMock = {
    "status": 200,
    "data": {
        "items": [GetSingleArticleMock],
        "count": 0,
        "limit": 0,
    },
}
