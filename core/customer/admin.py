from django.contrib import admin

from core.customer.models import customers

# Register your models here.
from .models import Customer

admin.site.register(Customer)
