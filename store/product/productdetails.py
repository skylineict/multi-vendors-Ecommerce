from django.shortcuts import render
from django.views.generic import View
from django.db.models import Avg
from product.models import CartOrder, CartOrderItems,Category,Products,Productimage,ProductReview,Wishlist,orderaddress
import pdb


class ProductDetails(View):
    def get(self,request, product_id):
        productdetails = Products.objects.get(product_id=product_id)
        feature_image = Productimage.objects.filter(product_names=productdetails)
        related_product = Products.objects.filter(category=productdetails.category).exclude(product_id=product_id)
        # pdb.set_trace()
        product_review = ProductReview.objects.filter(product=productdetails).order_by('-date')

        product_rating = ProductReview.objects.filter(product=productdetails).aggregate(rating=Avg('rating'))
        # five_star_reviews = ProductReview.objects.filter(product=productdetails, rating=2)
     

     

        feature_images = productdetails.product_images.all
        context = {

           
            'productdetails': productdetails,
            'feature_image': feature_image,
            'feature_images': feature_images,
            'related_products':related_product,
            'product_reviews':product_review,
            'product_ratings': product_rating,
           


            
        }

       
       
       
        return render(request, 'shop/product_datails.html', context=context)
    


    def post(self,request):
        return render(request, 'shop/product_datails.html')
    


