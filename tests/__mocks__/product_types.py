from spreadconnect_python_sdk.models.products import ProductTypes
from spreadconnect_python_sdk.models.size_chart import SizeChart
from spreadconnect_python_sdk.models.categories import Categories, CategoryNode, Feature, BrandCategory, Gender
from spreadconnect_python_sdk.models.views import Views, View, ViewHotspot, ViewImage
from spreadconnect_python_sdk.models.preview import Preview, PreviewImage

GetProductTypesResponseMock = [
    ProductTypes(id="10", customer_name="Test Product")
]

GetSingleProductTypeResponseMock = ProductTypes(
    id="10",
    customer_name="Test Product",
    customer_description="desc"
)

SizeChartResponseMock = SizeChart(
    size_image_url="image-url.png",
    sizes=[]
)

GetProductTypeCategoriesResponseMock = Categories(
    categories=[
        CategoryNode(
            id="root", translation="Root Category",
            children=[CategoryNode(id="child", translation="Child")]
        )
    ],
    features=[Feature(id="feat1", translation="Feature")],
    brands=[BrandCategory(id="b1", translation="Brand")],
    genders=[Gender(id="g1", translation="Unisex")]
)

GetProductTypeViewsResponseMock = Views(
    views=[
        View(
            id="front",
            name="FRONT",
            hotspots=[ViewHotspot(name="CHEST_LEFT")],
            images=[ViewImage(appearance_id="1", image="image-url-front.png")]
        )
    ]
)

GetProductTypeDesignHotspotsResponseMock = {"hotspots": [{"name": "LEFT_CHEST"}, {"name": "BACK_CENTER"}]}

GetProductTypePreviewsResponseMock = Preview(
    images=[
        PreviewImage(url="preview-front.png", view_id="front", view_name="FRONT"),
        PreviewImage(url="preview-back.png", view_id="back", view_name="BACK")
    ]
)
