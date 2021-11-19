# # -*- coding: utf-8 -*-

from django import forms
from ..models import DeliveryBoy

# # -----------------------------------------------------------------------------
# # Users
# # -----------------------------------------------------------------------------


class MyDeliveryBoyCreationForm(forms.ModelForm):
    """Custom UserCreationForm."""

    class Meta:
        model = DeliveryBoy
        fields = [
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
            "payout_information",
            "vehical_info",
            "vehical_number",
            "vehical_photo",
            "aadhar_card",
            "pan_card",
            "driving_lincense",
            "per_order_charge",
            "activity_status",
            "order_accept_limit",
            "is_active",
        ]


class MyDeliveryBoyChangeForm(forms.ModelForm):
    """Custom UserChangeForm."""

    class Meta:
        model = DeliveryBoy
        fields = [
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
            "payout_information",
            "vehical_info",
            "vehical_number",
            "vehical_photo",
            "aadhar_card",
            "pan_card",
            "driving_lincense",
            "per_order_charge",
            "activity_status",
            "order_accept_limit",
            "is_active",
        ]
