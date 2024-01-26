from .views import ProductList,CategoryList,Category_product_list
from .productdetails import ProductDetails
from django.urls import path




urlpatterns = [
    
    path('', ProductList.as_view(),name="product_list"),
    path('category', CategoryList.as_view(),name="category_list"),
    path('category/<categoryid>',Category_product_list.as_view(),name="category_product"),
    path('product/<product_id>',ProductDetails.as_view(),name="productdatails"),

    
    
]