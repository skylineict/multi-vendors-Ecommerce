from django.urls import path
from .views import VendorsList
from .vendorstore import Vendor_Store




urlpatterns = [
    
    path('', VendorsList.as_view(),name="vendors"),
    path('vendorstore/<vendor_id>', Vendor_Store.as_view(), name='vendor_store')

     

    
    
]