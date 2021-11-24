# # -*- coding: utf-8 -*-

from django import forms
from ..models import Product, Category, SubCategory

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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["category"].queryset = Category.objects.filter(is_active=True)
        self.fields["subcategory"].queryset = SubCategory.objects.filter(is_active=True)
        for field in [
            "name",
            "category",
            "subcategory",
        ]:
            self.fields[field].required = True


class MyProductChangeForm(forms.ModelForm):
    """Custom UserChangeForm."""

    class Meta:
        model = Product
        fields = [
            "name",
            "alias",
            "category",
            "subcategory",
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["category"].queryset = Category.objects.filter(is_active=True)
        self.fields["subcategory"].queryset = SubCategory.objects.filter(is_active=True)
        for field in [
            "name",
            "category",
            "subcategory",
        ]:
            self.fields[field].required = True
