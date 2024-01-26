from django.shortcuts import render
from .models import Products,CartOrder,Category
from django.views.generic import View


# Create your views here.

class ProductList(View):
    
    
    def get(self,request):
        productlist = Products.objects.filter(product_status='approved')
        context = {

            'product_list': productlist
        }
       
        return render(request, 'shop/product_list.html', context=context)
    


    def post(self,request):
        return render(request, 'shop/product_list.html')
    




class CategoryList(View):
    
    
    def get(self,request):
        Categorylist = Category.objects.all()
        lasted_category = Category.objects.order_by('-date')[:4]
        context = {

            'categroylist': Categorylist,
            'lasted_category':lasted_category
        }
       
        return render(request, 'shop/categorylist.html', context=context)
    


    def post(self,request):
        return render(request, 'shop/categorylist.html')
    



class Category_product_list(View):
    
    
    def get(self,request,categoryid):
        Categorylist = Category.objects.get(categoryid=categoryid)
        product_category = Products.objects.filter(product_status='approved',category=Categorylist)
        context = {

            'product_category': product_category,
            'Categorylist': Categorylist
            
        }
       
        return render(request, 'shop/product_category_list.html', context=context)
    


    def post(self,request):
        return render(request, 'shop/product_category_list.html')
    


    