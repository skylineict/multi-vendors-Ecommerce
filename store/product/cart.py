
from django.http import JsonResponse
from .models import Products
import pdb
from django.shortcuts import render,redirect
from django.contrib import messages
from django.template.loader import render_to_string
import logging

logger = logging.getLogger(__name__)

def add_cart(request):
    new_cart = {}

    new_cart[str(request.GET['id'])] ={
        'item_quantity': request.GET['qty'],
        'product_name': request.GET['product_name'],
        'price': request.GET['price'],
        'image': request.GET['image'],
        'product_pid': request.GET['product_pid'],
        
        
        }
    
    
    
 
    
    if 'shop_cart_store' in request.session:
        if str(request.GET['id']) in request.session['shop_cart_store']:
            cart_data = request.session['shop_cart_store']
            cart_data[str(request.GET['id'])]['item_quantity'] = int(new_cart[str(request.GET['id'])]['item_quantity'])
            cart_data.update(cart_data)
            request.session['shop_cart_store'] = cart_data
        else:
            cart_data = request.session['shop_cart_store'] 
            cart_data.update(new_cart)
            request.session['shop_cart_store'] = cart_data

    else:
        request.session['shop_cart_store'] = new_cart

    return JsonResponse({
        'data':request.session['shop_cart_store'],
        'total_item':len(request.session['shop_cart_store'])
    })

# product_total_amount = 0


def veiw_add(request):
    tax  = 0
    product_total_amount = 0
    if 'shop_cart_store' in request.session:
        for product_id, item in request.session['shop_cart_store'].items():
            product_total_amount += int(item['item_quantity']) * float(item['price'])
            tax = product_total_amount * 6 / 100
       
            # total_after_vat =   product_total_amount + tax

        return render(request, 'shop/add_view.html',{'cart_data':request.session['shop_cart_store'],'total_item':len(request.session['shop_cart_store']), 'product_total_amount':product_total_amount, 'tax':tax})
    
    else:
        messages.info(request, "your cart is empty")
        return redirect('home')



def delete_cart(request):
    
    product_id = str(request.GET['id'])

    if 'shop_cart_store' in request.session:
        if product_id  in  request.session['shop_cart_store']:
            cart_data = request.session['shop_cart_store']
            del request.session['shop_cart_store'][product_id]
            request.session['shop_cart_store'] = cart_data
            # logger.info('Updated session data: %s', request.session.get('shop_cart_store'))
       
        
    tax = 0
    product_total_amount = 0
    if 'shop_cart_store' in request.session:
        for product_id, item in request.session['shop_cart_store'].items():
            product_total_amount += int(item['item_quantity']) * float(item['price'])
            tax = product_total_amount * 6 / 100
            # total_after_vat =   product_total_amount + tax
                # logger.info('Updated session data: %s', request.session.get('shop_cart_store'))
    context = render_to_string('shop/cartlist.html', {'cart_data':request.session['shop_cart_store'],'total_item':len(request.session['shop_cart_store']), 'product_total_amount':product_total_amount, 'tax':tax})
    return JsonResponse({"data": context,'total_item':len(request.session['shop_cart_store'])})
    





#update view item here



def update_cart(request):
    
    product_id = str(request.GET['id'])
    product_qty = str(request.GET['qty'])

    if 'shop_cart_store' in request.session:
        if product_id  in  request.session['shop_cart_store']:
            cart_data = request.session['shop_cart_store']
            cart_data[str(request.GET['id'])]['item_quantity'] = product_qty
            # del request.session['shop_cart_store'][product_id]
            request.session['shop_cart_store'] = cart_data
            # logger.info('Updated session data: %s', request.session.get('shop_cart_store'))
       
        
    tax = 0
    product_total_amount = 0
    if 'shop_cart_store' in request.session:
        for product_id, item in request.session['shop_cart_store'].items():
            product_total_amount += int(item['item_quantity']) * float(item['price'])
            tax = product_total_amount * 6 / 100
            # total_after_vat =   product_total_amount + tax
                # logger.info('Updated session data: %s', request.session.get('shop_cart_store'))
    context = render_to_string('shop/cartlist.html', {'cart_data':request.session['shop_cart_store'],'total_item':len(request.session['shop_cart_store']), 'product_total_amount':product_total_amount, 'tax':tax})
    return JsonResponse({"data": context,'total_item':len(request.session['shop_cart_store'])})
    








           
#this is the view for updating product in request.session
# def update_product(request):
#     item_quantity = request.GET['qty']
#     product_id = request.GET['id']
#     # logger.info('Received product ID: %s, Quantity: %s', product_id,item_quantity)
   
#     if 'shop_cart_store' in request.session:
#         if product_id  in  request.session['shop_cart_store']:
#             cart_data = request.session['shop_cart_store']
#             cart_data[str(request.GET['id'])]['qty'] = item_quantity
#             request.session['shop_cart_store'] = cart_data
#         # logger.info('Updated session data: %s', request.session.get('shop_cart_store'))
    

#     tax = 0
#     product_total_amount = 0
#     if 'shop_cart_store' in request.session:
#         for product_id, item in request.session['shop_cart_store'].items():
#             product_total_amount += int(item['item_quantity']) * float(item['price'])
#             tax = product_total_amount * 6 / 100
#             # total_after_vat =   product_total_amount + tax
#     context = render_to_string('shop/cartlist.html', {'cart_data':request.session['shop_cart_store'],'total_item':len(request.session['shop_cart_store']), 'product_total_amount':product_total_amount, 'tax':tax, "item_quantity":product_id})
#     return JsonResponse({"data": context,'total_item':len(request.session['shop_cart_store'])})





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
        