from core.customer.models import customers
from django.contrib import admin

# Register your models here.
from .models import Customer, CustomerWallet, CustomerWalletHistory, Membership

admin.site.register(Customer)
admin.site.register(Membership)
admin.site.register(CustomerWallet)
admin.site.register(CustomerWalletHistory)
