from django.views.generic import View
from django.shortcuts import render,redirect
from django.views.generic import View
from django.contrib.auth.models import User
from django.contrib  import messages
from django.contrib.auth import authenticate, login



class Login(View):
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