# # -*- coding: utf-8 -*-

from django import forms
from ..models import Customer

# # -----------------------------------------------------------------------------
# # Users
# # -----------------------------------------------------------------------------


class MyCustomerCreationForm(forms.ModelForm):
    """Custom UserCreationForm."""

    class Meta:
        model = Customer
        fields = [
            "email",
            "username",
            "first_name",
            "last_name",
            "profile_image",
            "description",
            "address",
            "city",
            "state",
            "country",
            "pincode",
            "is_active",
        ]


class MyCustomerChangeForm(forms.ModelForm):
    """Custom UserChangeForm."""

    class Meta:
        model = Customer
        fields = [
            "email",
            "username",
            "first_name",
            "last_name",
            "profile_image",
            "description",
            "address",
            "city",
            "state",
            "country",
            "pincode",
            "is_active",
        ]
