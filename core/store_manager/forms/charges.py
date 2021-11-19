# # -*- coding: utf-8 -*-

from django import forms
from ..models import DeliveryCharge

# # -----------------------------------------------------------------------------
# # Users
# # -----------------------------------------------------------------------------


class MyDeliveryChargeCreationForm(forms.ModelForm):
    """Custom UserCreationForm."""

    class Meta:
        model = DeliveryCharge
        fields = [
            "min_amount",
            "max_amount",
            "charge_amount",
        ]


class MyDeliveryChargeChangeForm(forms.ModelForm):
    """Custom UserChangeForm."""

    class Meta:
        model = DeliveryCharge
        fields = [
            "min_amount",
            "max_amount",
            "charge_amount",
        ]
