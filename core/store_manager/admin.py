from django.contrib import admin

# Register your models here.
from .models import (
    Category,
    Coupon,
    Expense,
    ExpenseType,
    Plan,
    Product,
    StoreProduct,
    Store,
    SubCategory,
    Order,
)

admin.site.register(Store)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Product)
admin.site.register(StoreProduct)
admin.site.register(Coupon)
admin.site.register(Expense)
admin.site.register(ExpenseType)
admin.site.register(Plan)
admin.site.register(Order)
