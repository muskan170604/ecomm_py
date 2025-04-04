from django.contrib import admin
from . models import Customer, Payment,Product,Cart,OrderPlaced

# Register your models here.

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display=['id','title','discounted_price','category','product_image']

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display=['id','user','locality','city','state','zipcode']
    
@admin.register(Cart)
class cartModelAdmin(admin.ModelAdmin):
    list_display=['id','user','product','quantity']
    
@admin.register(Payment)
class PaymentModelAdmin(admin.ModelAdmin):
    list_display=['id','user','amount','razorpay_order_id','razorpay_payment_status','razorpay_payment_id','paid']
    
@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display=['id','user','customer','product','quantity','status','payment']