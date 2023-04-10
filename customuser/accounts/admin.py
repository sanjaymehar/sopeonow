from django.contrib import admin

from .models import Seller,Customer,Admin

# Register your models here.
admin.site.register(Seller)
admin.site.register(Customer)
admin.site.register(Admin)
