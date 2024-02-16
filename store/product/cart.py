
from django.http import JsonResponse
from .models import Products
import pdb
from django.shortcuts import render,redirect
from django.contrib import messages
from django.template.loader import render_to_string
import logging
from django.urls import reverse
from django.shortcuts import render
from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings
from .models import  CartOrderItems, CartOrder
from django.contrib.auth.decorators  import login_required
import uuid
import random
import string
from .form import FlutterWavePaymentForm
from rave_python import Rave
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


@login_required
def checkout(request):
    tax = 0
    product_total_amount = 0
    total_with_tax =0
    
    if 'shop_cart_store' in request.session:
        # Check if there is an existing pending order for the user
        order_details = CartOrder.objects.filter(user=request.user, paid_status=False).first()
        
        if not order_details:
           
            # Create a new order if one doesn't exist
            order_details = CartOrder.objects.create(user=request.user, paid_status=False, price=0,invoice_No=''.join(random.choices(string.ascii_uppercase + string.digits, k=10)), )
        
        # Calculate total amount and tax
        for product_id, item in request.session['shop_cart_store'].items():
            product_total_amount += int(item['item_quantity']) * float(item['price'])
            tax = product_total_amount * 6 / 100
            total_with_tax = tax + product_total_amount
            
            # Create CartOrderItems object for each item in the cart
            orderitem =  CartOrderItems.objects.create(
                order=order_details,
                item=item['product_name'],
                image=item['image'],  # Assuming you store the image URL
                price=item['price'],
                total=total_with_tax,
                qty=item['item_quantity'],
                invoice_No = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10)),  # Adjust as needed

    
            )
        ip_address =  request.META.get('REMOTE_ADDR') 
        
        order_details.price = total_with_tax
        order_details.save()
        
        host = request.get_host()
        order_items = CartOrder.objects.get(user=request.user)
        # url =  'http://{}{}'.format(host,reverse('payment-success'))


        
        return render(request, 'shop/checkout.html', {
            'cart_data': request.session['shop_cart_store'],
            'total_item': len(request.session['shop_cart_store']),
            'product_total_amount': product_total_amount,
            'tax': tax,'order_items':order_items, 'ip_address':ip_address
           
        })
    else:
        # Handle case when cart is empty
        return redirect('home')




@login_required
def payment_sucessfuly(request,pk):
    orders = CartOrder.objects.get(pk=pk)
    orders.paid_status = True
    orders.save()
    if 'shop_cart_store' in request.session:
        del request.session['shop_cart_store']
           
    return render(request,"payment/succes.html")

@login_required
def payment_failled(request):
    return render(request,"payment/failled.html")

           
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
    # tax = 0
    # product_total_amount = 0
    # if 'shop_cart_store' in request.session:
    #     for product_id, item in request.session['shop_cart_store'].items():
    #         product_total_amount += int(item['item_quantity']) * float(item['price'])
    #         tax = product_total_amount * 6 / 100
    #         total_with_tax = tax + product_total_amount

    #     product_order = CartOrder.objects.create(user=request.user,price=total_with_tax)

    # for product_id, item in request.session['shop_cart_store'].items():
    #     product_total_amount += int(item['item_quantity']) * float(item['price'])
    #     tax = product_total_amount * 6 / 100
    #     total_with_tax = tax + product_total_amount
    #     cart_order_item = CartOrderItems.objects.create(order=product_order, 
    #     invoice_No= ''.join(random.choices(string.ascii_uppercase + string.digits, k=10)),
    #     price=item['price'],
    #     image=item['image'],
    #     item=item['product_name'],
    #     qty=item['item_quantity'],
    #     total=total_with_tax )
    
    # host = request.get_host()
    # paypal_dict = {
    #     "business": settings.PAYPAL_RECEIVER_EMAIL,
    #     "amount": product_order.price,
    #     "item_name": item['product_name'],
    #     "invoice": cart_order_item.invoice_No,
    #     "notify_url": request.build_absolute_uri(reverse('paypal-ipn')),
    #     "return":   'http://{}{}'.format(host,reverse('payment-success')),
    #     "cancel_return":'http://{}{}'.format(host,reverse('payment-failled')),
    #     # "custom": "premium_plan",  # Custom command to correlate to some function later (optional)
    #  }

    # paypal_paymentform = PayPalPaymentsForm(initial=paypal_dict)

# @login_required
# def checkout(request):
#     rave =  Rave(public_key='FLWPUBK_TEST-1a46d81af91bb55a3664bf37222ee465-X', secret_key='FLWSECK_TEST-ca16b17b2f5472af8b5939e71e72af61-X', environment='sandbox',usingEnv = False)  # Initialize FlutterWave with your credentials
    
#       # Check if there is an existing pending order for the user
   
        
#     tax = 0
#     product_total_amount = 0
#     total_with_tax = 0
#     if 'shop_cart_store' in request.session:
#         for product_id, item in request.session['shop_cart_store'].items():
#             product_total_amount += int(item['item_quantity']) * float(item['price'])
#             tax = product_total_amount * 6 / 100
#             total_with_tax = tax + product_total_amount
#         order_details = CartOrder.objects.filter(user=request.user, paid_status=False).first()
#         if not order_details:
#             # Create a new order if one doesn't exist
#             order_details = CartOrder.objects.get_or_create(user=request.user,price=total_with_tax,  paid_status=False)
#          # Proceed with the checkout process
#         flutterwave_payment_form = FlutterWavePaymentForm(request.POST or None)
        
#         if request.method == 'POST' and flutterwave_payment_form.is_valid():
#             card_number = flutterwave_payment_form.cleaned_data['card_number']
#             expiration_date = flutterwave_payment_form.cleaned_data['expiration_date']
#             cvv = flutterwave_payment_form.cleaned_data['cvv']
#         host = request.get_host()
#         payment_data = {
#                 'amount': total_with_tax,
#                 'currency': 'USD',
#                 'redirect_url': 'http://{}{}'.format(host,reverse('payment-success')),
#                 'tx_ref': 'unique_transaction_reference',
                  
#                     # Specify your redirect URL for payment completion
#                 # You can add more parameters as required by Flutterwave
#             }
        
#         payment_response = rave.Card.charge(
#                 card_number=card_number, 
#                 cvv=cvv, 
#                 expiry_month=expiration_date.split('/')[0], 
#                 expiry_year=expiration_date.split('/')[1], 
#                 **payment_data
#             )
        

            
        
        

#         return render(request,'shop/checkout.html', {'cart_data':request.session['shop_cart_store'],'total_item':len(request.session['shop_cart_store']), 'product_total_amount':product_total_amount, 'tax':tax, })
    
#     else:
#         return redirect('home')
# ave =  Rave('FLWPUBK_TEST-1a46d81af91bb55a3664bf37222ee465-X', 'FLWSECK_TEST-ca16b17b2f5472af8b5939e71e72af61-X',usingEnv = False)  # Initialize FlutterWave with your credentials  
# def checkout(request):
#     tax = 0
#     product_total_amount = 0
#     total_with_tax =0
    
#     if 'shop_cart_store' in request.session:
#         # Check if there is an existing pending order for the user
#         order_details = CartOrder.objects.filter(user=request.user, paid_status=False).first()
        
#         if not order_details:
#             # Create a new order if one doesn't exist
#             order_details = CartOrder.objects.create(user=request.user, paid_status=False, price=0)
        
#         # Calculate total amount and tax
#         for product_id, item in request.session['shop_cart_store'].items():
#             product_total_amount += int(item['item_quantity']) * float(item['price'])
#             tax = product_total_amount * 6 / 100
#             total_with_tax = tax + product_total_amount
            
#             # Create CartOrderItems object for each item in the cart
#             orderitem =  CartOrderItems.objects.create(
#                 order=order_details,
#                 item=item['product_name'],
#                 image=item['image'],  # Assuming you store the image URL
#                 price=item['price'],
#                 total=total_with_tax,
#                 qty=item['item_quantity'],
#                 invoice_No = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10)),  # Adjust as needed

    
#             )
#         # Update the order price with the calculated total amount
#         order_details.price = total_with_tax
#         order_details.save()
        
#         # Proceed with the checkout process
#         flutterwave_payment_form = FlutterWavePaymentForm(request.POST or None)
        
#         if request.method == 'POST' and flutterwave_payment_form.is_valid():
#             card_number = flutterwave_payment_form.cleaned_data['card_number']
#             expiration_date = flutterwave_payment_form.cleaned_data['expiration_date']
#             cvv = flutterwave_payment_form.cleaned_data['cvv']
            
#             # Create payment request data
#             host = request.get_host()
#             # payment_data = {
#             #     'amount': order_details.price,
#             #     'currency': 'NGN',
#             #     'redirect_url':  'http://{}{}'.format(host,reverse('payment-success')), 
#             #     'item_name': item['product_name'],
#             #      "invoice": orderitem.invoice_No
    
#             #     # Specify your redirect URL for payment completion
#             #     # You can add more parameters as required by Flutterwave
#             # }


#             payload = {
#                     'cardno': card_number,
#                     'redirect_url':  'http://{}{}'.format(host,reverse('payment-success')), 
#                     'cvv': cvv,
#                     'currency': 'NGN',  # Adjust currency as needed
#                     'expirymonth': expiration_date.split('/')[0],
#                     'expiryyear': expiration_date.split('/')[1],
#                     'amount': order_details.price,
#                     'email': request.user.email,
#                     'phonenumber': '08101523945',  # Adjust phone number as needed
#                     'firstname': request.user.first_name,
#                     'lastname': request.user.last_name,
#                     "invoice": orderitem.invoice_No,
#                     'IP': request.META.get('REMOTE_ADDR')  # Get user IP address
#                 }
#             payment_response  =  rave.Card.charge(payload)
#             # Charge payment using Flutterwave
#             # payment_response = rave.Card.charge(
#             #     card_number=card_number,
#             #     cvv=cvv,
#             #     expiry_month=expiration_date.split('/')[0],
#             #     expiry_year=expiration_date.split('/')[1],
#             #     **payment_data
#             # 

                   
            
#             # if payment_response['status'] == 'successful':
#                 # Payment successful
#                 # Update order status to paid
#             order_details.paid_status = True
#             order_details.save()
#             return redirect('payment-success')  # Redirect to payment success page
           
#                 # Payment failed
#                 # Display error message to the user
#             # return render(request, 'shop/payment_failed.html', {'error_message': payment_response['message']})
        
#         return render(request, 'shop/checkout.html', {
#             'cart_data': request.session['shop_cart_store'],
#             'total_item': len(request.session['shop_cart_store']),
#             'product_total_amount': product_total_amount,
#             'tax': tax,
#             'flutterwave_payment_form': flutterwave_payment_form
#         })
#     else:
#         # Handle case when cart is empty
#         return redirect('home')
