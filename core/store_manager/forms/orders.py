# # -*- coding: utf-8 -*-

from django import forms
from ..models import Order

# # -----------------------------------------------------------------------------
# # Users
# # -----------------------------------------------------------------------------


class MyOrderCreationForm(forms.ModelForm):
    """Custom UserCreationForm."""

    class Meta:
        model = Order
        fields = [
            "order_status",
            "customer",
            "store",
            "product",
            "total_qty",
            "total_amount",
            "order_datetime",
            "status",
            "reason",
            "payment_method",
            "discount_amount",
            "shipping_charge",
            "shipping_address",
            "coupon",
            "discount_type",
            "order_number",
            "billing_number",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # for field in self.fields:
        #     self.fields[field].required = True


class MyOrderChangeForm(forms.ModelForm):
    """Custom UserChangeForm."""

    class Meta:
        model = Order
        fields = [
            "order_status",
            "customer",
            "store",
            "product",
            "total_qty",
            "total_amount",
            "order_datetime",
            "status",
            "reason",
            "payment_method",
            "discount_amount",
            "shipping_charge",
            "shipping_address",
            "coupon",
            "discount_type",
            "order_number",
            "billing_number",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # for field in self.fields:
        #     self.fields[field].required = True
