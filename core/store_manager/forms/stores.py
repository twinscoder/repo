# # -*- coding: utf-8 -*-

from django import forms
from ..models import Store

# # -----------------------------------------------------------------------------
# # Users
# # -----------------------------------------------------------------------------


class MyStoreCreationForm(forms.ModelForm):
    """Custom UserCreationForm."""

    class Meta:
        model = Store
        fields = [
            "name",
            "business_email",
            "phone",
            "image",
            "description",
            "address",
            "city",
            "state",
            "country",
            "pincode",
            "account_name",
            "account_number",
            "bank_name",
            "branch_name",
            "branch_address",
            "ifsc_code",
            "upi_qr_code",
            "is_active",
        ]


class MyStoreChangeForm(forms.ModelForm):
    """Custom UserChangeForm."""

    class Meta:
        model = Store
        fields = [
            "name",
            "business_email",
            "phone",
            "image",
            "description",
            "address",
            "city",
            "state",
            "country",
            "pincode",
            "account_name",
            "account_number",
            "bank_name",
            "branch_name",
            "branch_address",
            "ifsc_code",
            "upi_qr_code",
            "is_active",
        ]
