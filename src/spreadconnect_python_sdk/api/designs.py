from typing import Dict, Any
from spreadconnect_python_sdk.http.client import HttpClient
from spreadconnect_python_sdk.endpoints import DESIGNS_PATH
from spreadconnect_python_sdk.models.designs import DesignUpload, DesignUploadResponse


class DesignsApi:
    """
    Provides access to the `/designs` endpoints of the Spreadconnect API.
    """

    def __init__(self, client: HttpClient) -> None:
        """
        Initialize the Designs API client.

        Parameters
        ----------
        client : HttpClient
            The shared HTTP client instance used for making requests.
        """
        self._client = client

    def upload(self, design: DesignUpload) -> DesignUploadResponse:
        """
        Upload a new design to Spreadconnect.

        This can be done by:
        - uploading a binary file (PNG, < 10MB), or
        - providing a public image URL, which Spreadconnect will fetch.

        Sends a POST request to `/designs/upload` using multipart/form-data.

        Parameters
        ----------
        design : DesignUpload
            The design upload details.
            - `file`: The binary file/image to upload (bytes or file-like).
            - `url`: Optional public image URL to fetch.

        Returns
        -------
        DesignUploadResponse
            Contains a reusable `design_id` that can be referenced in other APIs.
        """
        files: Dict[str, Any] = {}
        data: Dict[str, Any] = {}

        if design.file:
            files["file"] = ("file.png", design.file, "image/png")
        if design.url:
            data["url"] = design.url

        return self._client.request(
            "POST",
            f"{DESIGNS_PATH}/upload",
            response_model=DesignUploadResponse,
            files=files if files else None,
            data=data if data else None,
        )
