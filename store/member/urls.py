from .views import Registration
from django.urls import path
from .userlogin import Login
from .logout import Logout



urlpatterns = [
    
    path('', Registration.as_view(),name="register"),
    path('login', Login.as_view(),name="login"),
    path('loginout', Logout.as_view(),name="logout"),
    
    
]