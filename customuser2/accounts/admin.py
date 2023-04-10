from django.contrib import admin

from .models import User,Seller,Customer,Admin,Delivery

# Register your models here.
admin.site.register(User)
admin.site.register(Seller)
admin.site.register(Customer)
admin.site.register(Admin)
admin.site.register(Delivery)