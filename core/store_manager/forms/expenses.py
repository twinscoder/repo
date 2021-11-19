# # -*- coding: utf-8 -*-

from django import forms
from ..models import Expense, ExpenseType

# # -----------------------------------------------------------------------------
# # Users
# # -----------------------------------------------------------------------------


class MyExpenseTypeCreationForm(forms.ModelForm):
    """Custom UserCreationForm."""

    class Meta:
        model = ExpenseType
        fields = [
            "name",
            "is_active",
        ]


class MyExpenseTypeChangeForm(forms.ModelForm):
    """Custom UserChangeForm."""

    class Meta:
        model = ExpenseType
        fields = [
            "name",
            "is_active",
        ]


class MyExpenseCreationForm(forms.ModelForm):
    """Custom UserCreationForm."""

    class Meta:
        model = Expense
        fields = [
            "type",
            "store",
            "amount",
            "description",
            "is_active",
        ]


class MyExpenseChangeForm(forms.ModelForm):
    """Custom UserChangeForm."""

    class Meta:
        model = Expense
        fields = [
            "type",
            "store",
            "amount",
            "description",
            "is_active",
        ]
