from spreadconnect_python_sdk.models.stocks import (
    GetStocksResponse,
    GetStockResponse,
    GetStockByProductTypeResponse,
    StockVariantByProductType,
)

StocksResponseMock = GetStocksResponse(
    items={"test": 10},
    count=10,
    limit=0,
    offset=0,
)

StockResponseMock = GetStockResponse(10)

GetStockByProductTypeResponseMock = GetStockByProductTypeResponse(
    variants=[
        StockVariantByProductType(appearance_id="1", size_id="M", stock=42),
        StockVariantByProductType(appearance_id="2", size_id="L", stock=10),
    ]
)
