from django.contrib import admin
from .models import customer, product, producttail, order, orderitem, shippingaddress
# Register your models here.
admin.site.register(customer)
admin.site.register(product)
admin.site.register(producttail)
admin.site.register(order)
admin.site.register(orderitem)
admin.site.register(shippingaddress)