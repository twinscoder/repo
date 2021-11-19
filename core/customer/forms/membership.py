# # -*- coding: utf-8 -*-

from django import forms
from ..models import Membership

# # -----------------------------------------------------------------------------
# # Users
# # -----------------------------------------------------------------------------


class MyMembershipCreationForm(forms.ModelForm):
    """Custom UserCreationForm."""

    class Meta:
        model = Membership
        fields = [
            "customer",
            "plan",
            "start_date",
            "end_date",
            "is_active",
        ]


class MyMembershipChangeForm(forms.ModelForm):
    """Custom UserChangeForm."""

    class Meta:
        model = Membership
        fields = [
            "customer",
            "plan",
            "start_date",
            "end_date",
            "is_active",
        ]
