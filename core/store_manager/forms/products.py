# # -*- coding: utf-8 -*-

from django import forms
from ..models import Product, Category, SubCategory, StoreProduct

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
            "small_description",
            "long_description",
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
            "small_description",
            "long_description",
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


# # -----------------------------------------------------------------------------
# # Users
# # -----------------------------------------------------------------------------


class MyStoreProductCreationForm(forms.ModelForm):
    """Custom UserCreationForm."""

    class Meta:
        model = StoreProduct
        fields = [
            "product",
            "store",
            "priority_index",
            "purchase_price",
            "selling_price",
            "membership_price",
            "stock",
            "unit",
            "cancel_available",
            "free_shipping",
            "cash_on_delivery",
            "is_active",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in [
            "store",
            "product",
            "purchase_price",
            "selling_price",
            "membership_price",
            "unit",
        ]:
            self.fields[field].required = True

    def clean_priority_index(self):
        """Normalize emails to lowercase."""
        priority_index = self.cleaned_data["priority_index"]
        store_product = StoreProduct.objects.filter(
            priority_index=priority_index
        ).first()
        print("➡ store_product :", store_product)
        store_product_count = StoreProduct.objects.all().count()
        print("➡ store_product_count :", store_product_count)
        if store_product:
            store_product.priority_index = store_product_count
            store_product.save()
            return priority_index
        else:
            return store_product_count


class MyStoreProductChangeForm(forms.ModelForm):
    """Custom UserChangeForm."""

    class Meta:
        model = StoreProduct
        fields = [
            "product",
            "store",
            "priority_index",
            "purchase_price",
            "selling_price",
            "membership_price",
            "stock",
            "unit",
            "cancel_available",
            "free_shipping",
            "cash_on_delivery",
            "is_active",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in [
            "store",
            "product",
            "purchase_price",
            "selling_price",
            "membership_price",
            "unit",
        ]:
            self.fields[field].required = True

    def clean_priority_index(self):
        """Normalize emails to lowercase."""
        priority_index = self.cleaned_data["priority_index"]
        store_product = StoreProduct.objects.filter(
            priority_index=priority_index
        ).first()
        store_product_count = StoreProduct.objects.all().count()
        if store_product:
            store_product.priority_index = store_product_count
            store_product.save()
            return priority_index
        else:
            return store_product_count
