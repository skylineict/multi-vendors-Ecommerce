
from django.http import JsonResponse
from .models import Products
import pdb

# def add_cart(request):
    
#     new_cart = {}

#     new_cart[str(request.GET['productid'])] ={
#         'item_quantity': request.GET['qty'],
#         'product_name': request.GET['product_name'],
#         'price': request.GET['price'],
#         }
    

#     return JsonResponse({ 'data':new_cart


#     })
    
 
    
    # if 'shop_cart_store' in request.session:
    #     if str(request.GET['productid']) in request.session['shop_cart_store']:
    #         cart_data = request.session['shop_cart_store']
    #         cart_data[str(request.GET['productid'])]['item_quantity'] = int(new_cart[str(request.GET['productid'])]['item_quantity'])
    #         cart_data.update(cart_data)
    #         request.session['shop_cart_store'] = cart_data
    #     else:
    #         cart_data = request.session['shop_cart_store'] 
    #         cart_data.update(new_cart)
    #         request.session['shop_cart_store'] = cart_data

    # else:
    #     request.session['shop_cart_store'] = new_cart

    # return JsonResponse({
    #     'data':request.session['shop_cart_store'],
    #     'totalitemadded':len(request.session['shop_cart_store'])
    # })


    






  #(1) #Checking if There's Already product in the Cart
    
    #(2) This line checks whether the item identified by its 'id' 
        # is already present 
        # in the shopping cart stored in the user's session
    
    #  (3)If the item is already in the cart, this line 
    # retrieves the existing cart data from the user's session.

    #  (4)This line updates the quantity of the existing item in the cart.
    # It converts the quantity from the newly added item 
    # (cart_p) to an integer and assigns it to the existing 
    # item in the cart.

    # (5)This line updates the cart_data
    # dictionary with the changes made 
    # in the previous 
    
    #(6)this line updates the shopping cart
    # in the user's session (shop_cart_store) with the
    # modified cart_data dictionary, 
    # reflecting the changes made to the existing item's quantity.
        