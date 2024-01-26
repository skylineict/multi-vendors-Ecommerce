from django.views.generic import View
from django.shortcuts import render,redirect
from django.views.generic import View
from django.contrib.auth.models import User
from django.contrib  import messages
from django.contrib.auth import authenticate, login

import pdb

# Create your views here.
class Registration(View):
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
    
        