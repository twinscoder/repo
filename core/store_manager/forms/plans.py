# # -*- coding: utf-8 -*-

from django import forms
from ..models import Plan

# # -----------------------------------------------------------------------------
# # Users
# # -----------------------------------------------------------------------------


class MyPlanForm(forms.ModelForm):
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].required = True