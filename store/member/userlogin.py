from django.views.generic import View
from django.shortcuts import render,redirect
from django.views.generic import View
from django.contrib.auth.models import User
from django.contrib  import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth import get_user_model
from .models import User





class Login(UserPassesTestMixin,View):
    def test_func(self):
        return not self.request.user.is_authenticated

    def handle_no_permission(self):
        return redirect('home')  # Redirect to 'dashboard' if the user is authenticated
  
    def get(self, request):
        return  render(request, 'users/login.html')
    
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
       
        # ison =  Profiles.objects.filter(user=request.user).exists()
        
        
        if not User.objects.filter(username=username).exists():
            messages.error(request, 'your username is invalid')
            return  render(request, 'users/login.html')
        if password and username:
            user = authenticate(username=username, password=password)
            
            if user:
                login(request,user)
                messages.success(request, 'login sucessully')
                return  redirect('home')
               
               
                
            
            messages.error(request, 'incorrect password try again')
            return  render(request, 'users/login.html')
        
     
        messages.error(request, "empty field not allowed")
        return  render(request, 'users/login.html')
        
        # return  render(request, 'login.html')