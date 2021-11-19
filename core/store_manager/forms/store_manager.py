# # -*- coding: utf-8 -*-

from django import forms
from ..models import StoreManager

# # -----------------------------------------------------------------------------
# # Users
# # -----------------------------------------------------------------------------


class MyStoreManagerCreationForm(forms.ModelForm):
    """Custom UserCreationForm."""

    class Meta:
        model = StoreManager
        fields = [
            "store",
            "first_name",
            "last_name",
            "gender",
            "birth_date",
            "email",
            "phone",
            "username",
            "profile_image",
            "description",
            "address",
            "city",
            "state",
            "country",
            "pincode",
            "is_active",
        ]


class MyStoreManagerChangeForm(forms.ModelForm):
    """Custom UserChangeForm."""

    class Meta:
        model = StoreManager
        fields = [
            "store",
            "first_name",
            "last_name",
            "gender",
            "birth_date",
            "email",
            "phone",
            "username",
            "profile_image",
            "description",
            "address",
            "city",
            "state",
            "country",
            "pincode",
            "is_active",
        ]
