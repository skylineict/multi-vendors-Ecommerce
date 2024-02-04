from django.shortcuts import render
from .models import  ProductReview,Products
from django.views.generic import View




class Search(View):
    def get(self, request):
         query = request.GET.get('search')
         products = Products.objects.filter(product_name__icontains=query)
         context = {
              'query':query,
              'product':products }
         return render(request,'shop/search.html',context=context)
    


    def post(self, request):
        #  query = request.POST['search']
        #  products = Products.objects.filter(product_name__icontains=query)
         

        #  context = {
        #       'query':query,
        #       'products':products

        #  }
 
    

         return render(request,'shop/search.html')