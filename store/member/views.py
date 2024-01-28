from django.views.generic import View
from django.shortcuts import render,redirect
from django.views.generic import View
from django.contrib.auth.models import User
from django.contrib  import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import user_passes_test
from .utiles import is_user_authenticated
from django.contrib.auth.mixins import UserPassesTestMixin


import pdb

# Create your views here.
class Registration(UserPassesTestMixin,View):
    def test_func(self):
        return not self.request.user.is_authenticated

    def handle_no_permission(self):
        return redirect('home')  # Redirect to 'dashboard' if the user is authenticated
  
    def get(self, request):
        return  render(request, 'users/register.html')
    

    def post(self, request):
        email = request.POST['email']
        password = request.POST['password']
        comfirm_password = request.POST['password2']
        username = request.POST['username']
        
        
        if password !=comfirm_password:
            messages.error(request, "Password Not the same")
            return  render(request, 'users/register.html')
        if len(password)  < 5:
            messages.error(request, "password too short try again")
            return  render(request, 'users/register.html')
        if User.objects.filter(email=email).exists():
            messages.error(request, "email has been taken try again")
            return  render(request, 'users/register.html')
        if User.objects.filter(username=username).exists():
            messages.error(request, "username has been taken")
            return  render(request, 'users/register.html')
        
        user = User.objects.create_user(email=email,username=username,password=password )
        user = authenticate(username=username, password=password)
        login(request,user)        
        messages.success(request, "Account created successfully and login")
        return redirect('home')
        return  render(request, 'users/register.html')
    
        