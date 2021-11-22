# # -*- coding: utf-8 -*-

from django import forms
from ..models import Category, SubCategory

# # -----------------------------------------------------------------------------
# # Users
# # -----------------------------------------------------------------------------


class MyCategoryForm(forms.ModelForm):
    """Custom UserCreationForm."""

    class Meta:
        model = Category
        fields = [
            "name",
            "image",
            "description",
            "is_active",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].required = True


class MySubCategoryForm(forms.ModelForm):
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["parent_category"].queryset = Category.objects.filter(
            is_active=True
        )
        for field in ["parent_category", "name"]:
            self.fields[field].required = True
