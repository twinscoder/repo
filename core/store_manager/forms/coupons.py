# # -*- coding: utf-8 -*-

from django import forms

from core.store_manager.models import category
from ..models import Coupon, Category, SubCategory, Product

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
        self.fields["category"].queryset = Category.objects.filter(is_active=True)
        self.fields["sub_category"].queryset = SubCategory.objects.filter(
            is_active=True
        ).filter(category__is_active=True)
        self.fields["product"].queryset = (
            Product.objects.filter(is_active=True)
            .filter(category__is_active=True)
            .filter(sub_category__is_active=True)
        )
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
        self.fields["category"].queryset = Category.objects.filter(is_active=True)
        self.fields["sub_category"].queryset = SubCategory.objects.filter(
            is_active=True
        ).filter(category__is_active=True)
        self.fields["product"].queryset = (
            Product.objects.filter(is_active=True)
            .filter(category__is_active=True)
            .filter(sub_category__is_active=True)
        )
        # for field in self.fields:
        #     self.fields[field].required = True
