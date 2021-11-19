# # -*- coding: utf-8 -*-

from django import forms
from ..models import Plan

# # -----------------------------------------------------------------------------
# # Users
# # -----------------------------------------------------------------------------


class MyPlanCreationForm(forms.ModelForm):
    """Custom UserCreationForm."""

    class Meta:
        model = Plan
        fields = [
            "name",
            "price",
            "description",
            "days",
            "months",
            "is_active",
        ]


class MyPlanChangeForm(forms.ModelForm):
    """Custom UserChangeForm."""

    class Meta:
        model = Plan
        fields = [
            "name",
            "price",
            "description",
            "days",
            "months",
            "is_active",
        ]
