
from .models import CartOrder, CartOrderItems,Category,Products,Productimage,ProductReview,Wishlist,orderaddress

def category_list(request):

    category_list = Category.objects.all()
    lasted_category = Category.objects.order_by('-date')[:6]




    return {
'category_list':category_list,
'lasted_category': lasted_category,
'myuser':    request.user



    }









