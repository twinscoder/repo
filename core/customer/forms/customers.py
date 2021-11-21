# # -*- coding: utf-8 -*-

from django import forms
from ..models import Customer
from core.customadmin.utils import refer_code_generator

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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].required = True

    def save(self, commit=True):
        instance = super().save(commit=False)

        if commit:
            instance.refer_code = refer_code_generator()
            instance.save()

        return instance


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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].required = True
