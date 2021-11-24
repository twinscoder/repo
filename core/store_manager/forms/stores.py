# # -*- coding: utf-8 -*-

from django import forms

from core.user.models.users import User
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
            "products",
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
        for field in ["name", "business_email", "store_manager"]:
            self.fields[field].required = True
        self.fields["store_manager"].queryset = User.objects.filter(role=User.MANAGER)


class MyStoreChangeForm(forms.ModelForm):
    """Custom UserChangeForm."""

    class Meta:
        model = Store
        fields = [
            "store_manager",
            "products",
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
        for field in ["name", "business_email", "store_manager"]:
            self.fields[field].required = True
