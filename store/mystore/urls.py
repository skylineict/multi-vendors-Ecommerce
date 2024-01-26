from .views import shop
from django.urls import path




urlpatterns = [
    
    path('', shop.as_view(),name="home"),
    
    
]