from .views import ProductList,CategoryList,Category_product_list
from .productdetails import ProductDetails, add_reveiw,add_cart
from django.urls import path
from .search import Search





urlpatterns = [
    
    path('', ProductList.as_view(),name="product_list"),
    path('category', CategoryList.as_view(),name="category_list"),
    path('category/<categoryid>',Category_product_list.as_view(),name="category_product"),
    path('product/<product_id>',ProductDetails.as_view(),name="productdatails"),
    path('add_reveiw/<product_id>',add_reveiw,name="add_reveiw"),
    #saerch
    path('search', Search.as_view(),name="search"),
    #addto adver
    path('add-to-cart',add_cart,name="add_cart")

    
    
]