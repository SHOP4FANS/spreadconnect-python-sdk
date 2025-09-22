import httpx
from typing import Any, Dict, Optional, Type, TypeVar, overload, Mapping, Tuple, Union, Sequence
from pydantic import BaseModel
from spreadconnect_python_sdk.exceptions import SpreadconnectError, OrderError
from spreadconnect_python_sdk.models.errors import ErrorResponse

T = TypeVar("T", bound=BaseModel)

FileTypes = Union[
    Tuple[str, Union[bytes, str]],
    Tuple[str, Union[bytes, str], str],
    Tuple[str, Union[bytes, str], str, Dict[str, str]],
]


class HttpClient:
    def __init__(self, base_url: str, token: str, timeout: Optional[int] = 30) -> None:
        self.base_url = base_url.rstrip("/")
        self.token = token
        self._client = httpx.Client(timeout=timeout)

    @overload
    def request(
        self,
        method: str,
        path: str,
        response_model: Type[T],
        *,
        json: Optional[Dict[str, Any]] = None,
        data: Optional[Dict[str, Any]] = None,
        files: Optional[Union[Mapping[str, FileTypes], Sequence[Tuple[str, FileTypes]]]] = None,
        query_params: Optional[Dict[str, Any]] = None,
    ) -> T: ...

    @overload
    def request(
        self,
        method: str,
        path: str,
        response_model: None = None,
        *,
        json: Optional[Dict[str, Any]] = None,
        data: Optional[Dict[str, Any]] = None,
        files: Optional[Union[Mapping[str, FileTypes], Sequence[Tuple[str, FileTypes]]]] = None,
        query_params: Optional[Dict[str, Any]] = None,
    ) -> Any: ...

    def request(
        self,
        method: str,
        path: str,
        response_model: Optional[Type[T]] = None,
        *,
        json: Optional[Dict[str, Any]] = None,
        data: Optional[Dict[str, Any]] = None,
        files: Optional[Union[Mapping[str, FileTypes], Sequence[Tuple[str, FileTypes]]]] = None,
        query_params: Optional[Dict[str, Any]] = None,
    ) -> Any:
        url = f"{self.base_url}{path}"
        headers = {"X-SPOD-ACCESS-TOKEN": self.token}

        response = self._client.request(
            method=method,
            url=url,
            headers=headers,
            params=query_params,
            json=json,
            data=data,
            files=files,
        )

        try:
            data_out = response.json()
        except Exception:
            data_out = None

        if not response.is_success:
            path_lower = path.lower()

            if path_lower.endswith("/confirm") or path_lower.endswith("/cancel"):
                try:
                    err = ErrorResponse.model_validate(data_out)
                except Exception:
                    err = ErrorResponse(reason=response.text)
                raise OrderError(response.status_code, err)

            raise SpreadconnectError(
                status_code=response.status_code,
                message=response.text,
                error=None,
            )

        if response_model and data_out is not None:
            return response_model.model_validate(data_out)
        return data_out
