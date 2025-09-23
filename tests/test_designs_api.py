import pytest
from unittest.mock import ANY
from spreadconnect_python_sdk.api.designs import DesignsApi
from spreadconnect_python_sdk.endpoints import DESIGNS_PATH
from spreadconnect_python_sdk.models.designs import DesignUpload
from tests.__mocks__.designs import DesignUploadPropsMock, DesignUploadResponseMock


def test_upload_design_with_url(mocker):
    mock_client = mocker.Mock()
    mock_client.request.return_value = DesignUploadResponseMock
    api = DesignsApi(mock_client)

    result = api.upload(DesignUploadPropsMock)

    assert result == DesignUploadResponseMock
    mock_client.request.assert_called_once_with(
        "POST",
        f"{DESIGNS_PATH}/upload",
        response_model=ANY,
        files=ANY,
        data=ANY,
    )


def test_upload_design_with_file(mocker):
    mock_client = mocker.Mock()
    mock_client.request.return_value = {
        "status": 200,
        "data": {"designId": "file-upload-id"},
    }
    api = DesignsApi(mock_client)

    file_bytes = b"hello"
    props = DesignUpload(file=file_bytes)

    result = api.upload(props)

    assert result == {
        "status": 200,
        "data": {"designId": "file-upload-id"},
    }
    mock_client.request.assert_called_once_with(
        "POST",
        f"{DESIGNS_PATH}/upload",
        response_model=ANY,
        files=ANY,
        data=ANY,
    )



def test_upload_design_raises_on_network_error(mocker):
    mock_client = mocker.Mock()
    mock_client.request.side_effect = Exception("Network Error")
    api = DesignsApi(mock_client)

    with pytest.raises(Exception) as exc:
        api.upload(DesignUploadPropsMock)

    assert "Network Error" in str(exc.value)
