from django.contrib import admin
from .models import CartOrder, CartOrderItems,Category,Products,Productimage,ProductReview,Wishlist,orderaddress
# Register your models here.


# Register your models here.

class ProductimageAdmin(admin.TabularInline):
    model = Productimage


admin.site.register(Productimage)





# Register your models here.
@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductimageAdmin]
    list_display = ['product_id','product_name','user','category','product_image',
                    'price','old_price','product_status','status',
                    'in_stock', 'digital']
    

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['categoryid','category_name','category_image', 'date']





@admin.register(CartOrder)
class CartorderAdmin(admin.ModelAdmin):
    list_display = ['paid_status','product_status','user','order_date','price','invoice_No',]



@admin.register(CartOrderItems)
class CartOrderItemsAdmin(admin.ModelAdmin):
    list_display = ['order','product_satus','item','image','total',
                    'price','qty','invoice_No']
    



@admin.register(ProductReview)
class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ['product','user','product','review','date',
                    'rating']
    


@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ['user','date','product']





@admin.register(orderaddress)
class orderaddressAdmin(admin.ModelAdmin):
    list_display = ['user','address','Status']