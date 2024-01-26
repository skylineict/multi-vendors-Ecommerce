from django.shortcuts import render
from .models import Vendor
from django.views.generic import View

# Create your views here.

class VendorsList(View):
    
    
    def get(self,request):
        vendors = Vendor.objects.all()
       
        context = {

            'vendors': vendors,
            
        }
       
        return render(request, 'vendors/vendors_list.html', context=context)
    


    def post(self,request):
        return render(request, 'vendors/vendors_list.html')
    


