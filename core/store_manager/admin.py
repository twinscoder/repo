from django.contrib import admin

# Register your models here.
from .models import Store, Category, Product, Coupon

admin.site.register(Store)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Coupon)
