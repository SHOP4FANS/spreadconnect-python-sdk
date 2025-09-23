from spreadconnect_python_sdk.models.designs import DesignUpload

DesignUploadPropsMock = DesignUpload(
    url="https://example.com/image.png"
)

DesignUploadResponseMock = {
    "status": 200,
    "data": {
        "designId": "mock-design-id-123",
    },
}
