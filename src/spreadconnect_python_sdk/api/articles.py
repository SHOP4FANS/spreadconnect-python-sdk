from typing import Optional
from spreadconnect_python_sdk.http.client import HttpClient
from spreadconnect_python_sdk.endpoints import ARTICLES_PATH
from spreadconnect_python_sdk.models.articles import (
    GetArticlesResponse,
    GetSingleArticleResponse,
    ArticleCreation,
    CreateArticleResponse,
    DeleteSingleArticleResponse,
)


class ArticlesApi:
    """
    Provides access to the `/articles` endpoints of the Spreadconnect API.
    """

    def __init__(self, client: HttpClient) -> None:
        """
        Initialize the Articles API client.

        Parameters
        ----------
        client : HttpClient
            The shared HTTP client instance used for making requests.
        """
        self._client = client

    def list(self, limit: Optional[int] = None, offset: Optional[int] = None) -> GetArticlesResponse:
        """
        Retrieve all articles from the point of sale.

        Sends a GET request to the `/articles` endpoint.

        Parameters
        ----------
        limit : int, optional
            The maximum number of results to return.
        offset : int, optional
            The offset to start retrieving records from.

        Returns
        -------
        GetArticlesResponse
            A list of articles with pagination metadata.
        """
        query = {}
        if limit is not None:
            query["limit"] = limit
        if offset is not None:
            query["offset"] = offset

        return self._client.request(
            "GET",
            ARTICLES_PATH,
            response_model=GetArticlesResponse,
            query_params=query or None,
        )

    def get(self, article_id: int) -> GetSingleArticleResponse:
        """
        Retrieve a specific article by its ID.

        Sends a GET request to the `/articles/{articleId}` endpoint.

        Parameters
        ----------
        article_id : int
            The ID of the article to retrieve.

        Returns
        -------
        GetSingleArticleResponse
            The details of the requested article.
        """
        return self._client.request(
            "GET",
            f"{ARTICLES_PATH}/{article_id}",
            response_model=GetSingleArticleResponse,
        )

    def create(self, props: ArticleCreation) -> CreateArticleResponse:
        """
        Create a new article in the point of sale.

        Sends a POST request to the `/articles` endpoint with the article data.
        Variants can define sizes and colors for the product.
        Configurations can place designs via URL (PNG format, < 10 MB).

        Parameters
        ----------
        props : ArticleCreation
            The article data to create.
            - `title`: The title of the article.
            - `description`: The description of the article.
            - `variants`: The variants of the article (sizes, colors).
            - `configurations`: The design configurations for the article.
            - `external_id`: Optional external ID for identifying the article.

        Returns
        -------
        CreateArticleResponse
            Contains the ID of the newly created article.
        """
        return self._client.request(
            "POST",
            ARTICLES_PATH,
            response_model=CreateArticleResponse,
            json=props.model_dump(exclude_none=True),
        )

    def delete(self, article_id: int) -> DeleteSingleArticleResponse:
        """
        Delete a specific article from the point of sale.

        Sends a DELETE request to the `/articles/{articleId}` endpoint.

        Parameters
        ----------
        article_id : int
            The ID of the article to delete.

        Returns
        -------
        DeleteSingleArticleResponse
            Empty response if the deletion was successful.
        """
        return self._client.request(
            "DELETE",
            f"{ARTICLES_PATH}/{article_id}",
            response_model=DeleteSingleArticleResponse,
        )
