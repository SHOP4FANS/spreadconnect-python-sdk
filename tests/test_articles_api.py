import pytest
from unittest.mock import ANY
from spreadconnect_python_sdk.api.articles import ArticlesApi
from spreadconnect_python_sdk.endpoints import ARTICLES_PATH
from tests.__mocks__.articles import (
    ArticleCreationMock,
    GetArticlesResponseMock,
    GetSingleArticleResponseMock,
)

def test_list_articles(mocker):
    mock_client = mocker.Mock()
    mock_client.request.return_value = GetArticlesResponseMock
    api = ArticlesApi(mock_client)

    result = api.list(limit=10, offset=0)

    assert result == GetArticlesResponseMock
    mock_client.request.assert_called_once_with(
        "GET",
        ARTICLES_PATH,
        response_model=ANY,
        query_params={"limit": 10, "offset": 0},
    )

def test_get_article(mocker):
    mock_client = mocker.Mock()
    mock_client.request.return_value = GetSingleArticleResponseMock
    api = ArticlesApi(mock_client)
    article_id = 10

    result = api.get(article_id)

    assert result == GetSingleArticleResponseMock
    mock_client.request.assert_called_once_with(
        "GET",
        f"{ARTICLES_PATH}/{article_id}",
        response_model=ANY,
    )

def test_create_article(mocker):
    mock_client = mocker.Mock()
    mock_client.request.return_value = GetSingleArticleResponseMock
    api = ArticlesApi(mock_client)

    result = api.create(ArticleCreationMock)

    assert result == GetSingleArticleResponseMock
    mock_client.request.assert_called_once_with(
        "POST",
        ARTICLES_PATH,
        response_model=ANY,
        json=ANY,
    )

def test_delete_article(mocker):
    mock_client = mocker.Mock()
    mock_client.request.return_value = None
    api = ArticlesApi(mock_client)
    article_id = 10

    result = api.delete(article_id)

    assert result is None
    mock_client.request.assert_called_once_with(
        "DELETE",
        f"{ARTICLES_PATH}/{article_id}",
        response_model=ANY,
    )

def test_get_article_raises_on_network_error(mocker):
    mock_client = mocker.Mock()
    mock_client.request.side_effect = Exception("Network Error")
    api = ArticlesApi(mock_client)

    with pytest.raises(Exception) as exc:
        api.get(42)

    assert "Network Error" in str(exc.value)
