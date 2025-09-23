import pytest
from unittest.mock import ANY
from spreadconnect_python_sdk.api.product_types import ProductTypesApi
from spreadconnect_python_sdk.endpoints import PRODUCT_TYPES_PATH
from tests.__mocks__.product_types import (
    GetProductTypesResponseMock,
    GetSingleProductTypeResponseMock,
    SizeChartResponseMock,
    GetProductTypeCategoriesResponseMock,
    GetProductTypeViewsResponseMock,
    GetProductTypeDesignHotspotsResponseMock,
    GetProductTypePreviewsResponseMock,
)


def test_list_product_types(mocker):
    mock_client = mocker.Mock()
    mock_client.request.return_value = GetProductTypesResponseMock
    api = ProductTypesApi(mock_client)

    res = api.list()

    assert res == GetProductTypesResponseMock
    mock_client.request.assert_called_once_with(
        "GET", PRODUCT_TYPES_PATH, response_model=ANY
    )


def test_get_single_product_type(mocker):
    mock_client = mocker.Mock()
    mock_client.request.return_value = GetSingleProductTypeResponseMock
    api = ProductTypesApi(mock_client)

    res = api.get("10")

    assert res == GetSingleProductTypeResponseMock
    mock_client.request.assert_called_once_with(
        "GET", f"{PRODUCT_TYPES_PATH}/10", response_model=ANY
    )


def test_get_size_chart(mocker):
    mock_client = mocker.Mock()
    mock_client.request.return_value = SizeChartResponseMock
    api = ProductTypesApi(mock_client)

    res = api.get_size_chart("10")
    assert res == SizeChartResponseMock
    mock_client.request.assert_called_once_with(
        "GET", f"{PRODUCT_TYPES_PATH}/10/size-chart", response_model=ANY
    )


def test_get_category_tree(mocker):
    mock_client = mocker.Mock()
    mock_client.request.return_value = GetProductTypeCategoriesResponseMock
    api = ProductTypesApi(mock_client)

    res = api.get_category_tree()
    assert res == GetProductTypeCategoriesResponseMock
    mock_client.request.assert_called_once_with(
        "GET", f"{PRODUCT_TYPES_PATH}/categories", response_model=ANY
    )


def test_get_categories_by_product_type(mocker):
    mock_client = mocker.Mock()
    mock_client.request.return_value = GetProductTypeCategoriesResponseMock
    api = ProductTypesApi(mock_client)

    res = api.get_categories_by_product_type("10")
    assert res == GetProductTypeCategoriesResponseMock
    mock_client.request.assert_called_once_with(
        "GET", f"{PRODUCT_TYPES_PATH}/10/categories", response_model=ANY
    )


def test_get_views(mocker):
    mock_client = mocker.Mock()
    mock_client.request.return_value = GetProductTypeViewsResponseMock
    api = ProductTypesApi(mock_client)

    res = api.get_views("10")
    assert res == GetProductTypeViewsResponseMock
    mock_client.request.assert_called_once_with(
        "GET", f"{PRODUCT_TYPES_PATH}/10/views", response_model=ANY
    )


def test_get_design_hotspots(mocker):
    mock_client = mocker.Mock()
    mock_client.request.return_value = GetProductTypeDesignHotspotsResponseMock
    api = ProductTypesApi(mock_client)

    res = api.get_design_hotspots("10", "123")
    assert res == GetProductTypeDesignHotspotsResponseMock
    mock_client.request.assert_called_once_with(
        "GET",
        f"{PRODUCT_TYPES_PATH}/10/hotspots/design/123",
        response_model=ANY,
    )


def test_get_previews(mocker):
    mock_client = mocker.Mock()
    mock_client.request.return_value = GetProductTypePreviewsResponseMock
    api = ProductTypesApi(mock_client)

    body = {"configurations": [{"designId": "123", "hotspot": "CHEST_LEFT"}]}
    res = api.get_previews("10", body)

    assert res == GetProductTypePreviewsResponseMock
    mock_client.request.assert_called_once_with(
        "POST",
        f"{PRODUCT_TYPES_PATH}/10/previews",
        response_model=ANY,
        json=body,
    )


def test_network_error_on_get(mocker):
    mock_client = mocker.Mock()
    mock_client.request.side_effect = Exception("Network Error")
    api = ProductTypesApi(mock_client)

    with pytest.raises(Exception) as exc:
        api.get("10")

    assert "Network Error" in str(exc.value)
