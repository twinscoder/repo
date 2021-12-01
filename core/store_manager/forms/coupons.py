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
            "discount_amount",
            "discount_percentage",
            "discount_type",
            "is_repeatable",
            "min_amount",
            "buy_product_count",
            "get_free_product_count",
            "description",
            "count",
            "category",
            "sub_category",
            "product",
            "instance_discount",
            "is_active",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # for field in self.fields:
        #     self.fields[field].required = True


class MyCouponChangeForm(forms.ModelForm):
    """Custom UserChangeForm."""

    class Meta:
        model = Coupon
        fields = [
            "code",
            "discount_amount",
            "discount_percentage",
            "discount_type",
            "is_repeatable",
            "min_amount",
            "buy_product_count",
            "get_free_product_count",
            "description",
            "count",
            "category",
            "sub_category",
            "product",
            "instance_discount",
            "is_active",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # for field in self.fields:
        #     self.fields[field].required = True
