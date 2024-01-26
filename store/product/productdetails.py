from django.shortcuts import render
from django.views.generic import View
from product.models import CartOrder, CartOrderItems,Category,Products,Productimage,ProductReview,Wishlist,orderaddress



class ProductDetails(View):
    def get(self,request, product_id):
        productdetails = Products.objects.get(product_id=product_id)
        feature_image = Productimage.objects.filter(product_names=productdetails)

        feature_images = productdetails.product_images.all
        context = {

           
            'productdetails': productdetails,
            'feature_image': feature_image,
            'feature_images': feature_images
            
        }
       
        return render(request, 'shop/product_datails.html', context=context)
    


    def post(self,request):
        return render(request, 'shop/product_datails.html')
    


