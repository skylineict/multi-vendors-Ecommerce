from django.shortcuts import render
from django.views.generic import View
from product.models import CartOrder, CartOrderItems,Category,Products,Productimage,ProductReview,Wishlist,orderaddress


class shop(View):
    
    
    def get(self,request):
        try: laptop_category = Category.objects.get(category_name='Laptop')
        except: laptop_category = None
        featues_product = Products.objects.filter(features=True, product_status='approved').order_by('-date')
        lasted_category = Category.objects.order_by('-date')[:4]
        context = {

            'features': featues_product,
            'lasted_category': lasted_category,
            'laptop_category':laptop_category
        }
       
        return render(request, 'shop/index.html', context=context)
    


    def post(self,request):
        return render(request, 'shop/index.html')

       