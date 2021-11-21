# # -*- coding: utf-8 -*-

from django import forms
from ..models import Coupon

# # -----------------------------------------------------------------------------
# # Users
# # -----------------------------------------------------------------------------


class MyCouponCreationForm(forms.ModelForm):
    """Custom UserCreationForm."""

    class Meta:
        model = Coupon
        fields = [
            "code",
            "amount",
            "discount_type",
            "is_repeatable",
            "min_amount",
            "max_amount",
            "start_date",
            "expiry_date",
            "description",
            "count",
            "is_active",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].required = True

class MyCouponChangeForm(forms.ModelForm):
    """Custom UserChangeForm."""

    class Meta:
        model = Coupon
        fields = [
            "code",
            "amount",
            "discount_type",
            "is_repeatable",
            "min_amount",
            "max_amount",
            "start_date",
            "expiry_date",
            "description",
            "count",
            "is_active",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].required = True