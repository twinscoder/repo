from django.contrib import admin

# Register your models here.
from .models import (
    DeliveryBoy,
    DeliveryBoyStatusHistory,
    DeliveryBoyWallet,
    DeliveryBoyWalletHistory,
)

admin.site.register(DeliveryBoy)
admin.site.register(DeliveryBoyStatusHistory)
admin.site.register(DeliveryBoyWallet)
admin.site.register(DeliveryBoyWalletHistory)
