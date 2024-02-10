from .views import ProductList,CategoryList,Category_product_list
from .productdetails import ProductDetails, add_reveiw
from django.urls import path
from .search import Search
from .cart import add_cart,veiw_add,delete_cart,update_cart




urlpatterns = [
    
    path('', ProductList.as_view(),name="product_list"),
    path('category', CategoryList.as_view(),name="category_list"),
    path('category/<categoryid>',Category_product_list.as_view(),name="category_product"),
    path('product/<product_id>',ProductDetails.as_view(),name="productdatails"),
    path('add_reveiw/<product_id>',add_reveiw,name="add_reveiw"),
    #saerch
    path('search', Search.as_view(),name="search"),
    #addto adver
    path('add-to-cart',add_cart,name="add_cart"),
    path('view_cart',veiw_add,name="view_cart"),
    path('delete_product_cart',delete_cart,name="delete-product_cart"),
    path('update_cart_item',update_cart,name="update_cart"),

   
   

    
    
]