# # -*- coding: utf-8 -*-

from django import forms
from ..models import Product

# # -----------------------------------------------------------------------------
# # Users
# # -----------------------------------------------------------------------------


class MyProductCreationForm(forms.ModelForm):
    """Custom UserCreationForm."""

    class Meta:
        model = Product
        fields = [
            "name",
            "alias",
            "category",
            "subcategory",
            "store",
            "coupon",
            "image",
            "description",
            "purchase_price",
            "selling_price",
            "membership_price",
            "stock",
            "unit",
            "cancel_available",
            "free_shipping",
            "cash_on_delivery",
            "is_deleted",
            "is_active",
        ]


class MyProductChangeForm(forms.ModelForm):
    """Custom UserChangeForm."""

    class Meta:
        model = Product
        fields = [
            "name",
            "alias",
            "category",
            "subcategory",
            "store",
            "coupon",
            "image",
            "description",
            "purchase_price",
            "selling_price",
            "membership_price",
            "stock",
            "unit",
            "cancel_available",
            "free_shipping",
            "cash_on_delivery",
            "is_deleted",
            "is_active",
        ]
