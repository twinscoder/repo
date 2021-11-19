# # -*- coding: utf-8 -*-

from django import forms
from ..models import Category, SubCategory

# # -----------------------------------------------------------------------------
# # Users
# # -----------------------------------------------------------------------------


class MyCategoryCreationForm(forms.ModelForm):
    """Custom UserCreationForm."""

    class Meta:
        model = Category
        fields = [
            "name",
            "image",
            "description",
            "is_active",
        ]


class MyCategoryChangeForm(forms.ModelForm):
    """Custom UserChangeForm."""

    class Meta:
        model = Category
        fields = [
            "name",
            "image",
            "description",
            "is_active",
        ]


class MySubCategoryCreationForm(forms.ModelForm):
    """Custom UserCreationForm."""

    class Meta:
        model = SubCategory
        fields = [
            "parent_category",
            "name",
            "image",
            "description",
            "is_active",
        ]


class MySubCategoryChangeForm(forms.ModelForm):
    """Custom UserChangeForm."""

    class Meta:
        model = SubCategory
        fields = [
            "parent_category",
            "name",
            "image",
            "description",
            "is_active",
        ]
