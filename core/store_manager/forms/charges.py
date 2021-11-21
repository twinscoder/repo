# # -*- coding: utf-8 -*-

from django import forms
from ..models import DeliveryCharge

# # -----------------------------------------------------------------------------
# # Users
# # -----------------------------------------------------------------------------


class MyDeliveryChargeForm(forms.ModelForm):
    """Custom UserCreationForm."""

    class Meta:
        model = DeliveryCharge
        fields = [
            "min_amount",
            "max_amount",
            "charge_amount",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].required = True

