from django.contrib import admin
from .models import product_master, sub_product

# Register your models here.

admin.site.register(product_master)
admin.site.register(sub_product)