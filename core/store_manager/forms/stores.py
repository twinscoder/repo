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
            "store_manager",
            "delivery_boys",
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in ["name", "business_email"]:
            self.fields[field].required = True


class MyStoreChangeForm(forms.ModelForm):
    """Custom UserChangeForm."""

    class Meta:
        model = Store
        fields = [
            "store_manager",
            "delivery_boys",
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in ["name", "business_email"]:
            self.fields[field].required = True
