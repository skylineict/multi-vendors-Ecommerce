
from .models import Vendor
from django.views.generic import View
from product.models import Products
from django.shortcuts import render



class Vendor_Store(View):
    
    
    def get(self,request,vendor_id):
        vendor = Vendor.objects.get(vendor_id=vendor_id)
        vendore_product = Products.objects.filter(product_status='approved',vendors=vendor )
        context = {

            'vendore_store': vendore_product,
            'vendor': vendor
            
        }
       
        return render(request, 'vendors/vendorstore.html', context=context)
    


    def post(self,request):
        return render(request, 'vendors/vendorstore.html')
    


    