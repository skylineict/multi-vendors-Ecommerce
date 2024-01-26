from django.views.generic import View
from django.shortcuts import render,redirect
from django.views.generic import View
from django.contrib.auth.models import User
from django.contrib  import messages
from django.contrib.auth import authenticate, login, logout





class Logout(View):
    def get(self,request):
        logout(request)
        messages.success(request,'logout sucessfully')
        return redirect('login')