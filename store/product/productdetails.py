from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from django.db.models import Avg
from django.http import Http404

from product.models import CartOrder, CartOrderItems,Category,Products,Productimage,ProductReview,Wishlist,orderaddress
import pdb
from .models import RATING_CHOICES

class ProductDetails(View):
    @staticmethod
    def get_star_rating(rating):
        return range(1, int(rating) + 1)
     
    def get(self,request, product_id):
        
      
        productdetails = Products.objects.get(product_id=product_id)
        feature_image = Productimage.objects.filter(product_names=productdetails)
        related_product = Products.objects.filter(category=productdetails.category).exclude(product_id=product_id)
     
        product_review = ProductReview.objects.filter(product=productdetails).order_by('-date')


        product_review = ProductReview.objects.filter(product=productdetails).order_by('-date')
      

        make_rview =True
        if request.user.is_authenticated:
            filter_veiw = ProductReview.objects.filter(user=request.user,product=productdetails).count()
            if filter_veiw > 0:
                make_rview = False

        # pdb.set_trace()
   
      

    
        # stars_list = ['*' * review.rating for review in product_review]
        

        product_rating = ProductReview.objects.filter(product=productdetails).aggregate(rating=Avg('rating'))
      
        # pdb.set_trace()

        feature_images = productdetails.product_images.all
        context = {

           
            'productdetails': productdetails,
            'make_rview': make_rview,
            'feature_image': feature_image,
            'feature_images': feature_images,
            'related_products':related_product,
            'product_reviews':product_review,
            'product_ratings': product_rating,
            'rating': RATING_CHOICES,
            'get_star_rating':   self.get_star_rating,
         
            
            
          


            
        }

       
       
       
        return render(request, 'shop/product_datails.html', context=context)
    


    def post(self,request,product_id):
        productdetails = Products.objects.get(product_id=product_id)
        feature_image = Productimage.objects.filter(product_names=productdetails)
        related_product = Products.objects.filter(category=productdetails.category).exclude(product_id=product_id)
        # pdb.set_trace()
        product_review = ProductReview.objects.filter(product=productdetails).order_by('-date')
        

        product_rating = ProductReview.objects.filter(product=productdetails).aggregate(rating=Avg('rating'))
      
     

        feature_images = productdetails.product_images.all
        context = {

           
            'productdetails': productdetails,
            'feature_image': feature_image,
            'feature_images': feature_images,
            'related_products':related_product,
            'product_reviews':product_review,
            'product_ratings': product_rating,
            'rating': RATING_CHOICES,
            
          


            
        }
        

     

   

        return render(request, 'shop/product_datails.html',context=context )
    


def add_reveiw(request,product_id):
    product = Products.objects.get(product_id=product_id)
    user = request.user
    comment = request.POST['comment']
    rating = request.POST['rating']

    review_create = ProductReview.objects.create(product=product,user=user,review=comment,rating=rating)
    product_rating = ProductReview.objects.filter(product=product).aggregate(rating=Avg('rating'))


    context = {

        'user': user.username,
        'comment': comment,
        'rating':  rating,
        
    }


    return JsonResponse({

        'bool': True,
        'context': context,
        'product_rating':product_rating


    })






def add_cart(request):
    
    new_cart = {}
    print(request.GET['id'])

    new_cart[(request.GET['id'])] ={
        'qty': request.GET['qty'],
        'product_name': request.GET['product_name'],
        'price': request.GET['price'],
        
        }
    

    return JsonResponse({ 'data':new_cart


    })





    


# class AddRevieiw(View):


#     def get(self,request, product_id):
#         return render(request, 'shop/product_datails.html', )
    
     



#     def post(self,request,product_id):
#         review   =  request.POST['rating']
#         comment =   request.POST['comment']
#         context = {


#             'comment':comment,
#             'review': review
#         }
#         products = Products.objects.get(product_id=product_id)
#         return render(request, 'shop/product_datails.html', context,context=context)
    