# # -*- coding: utf-8 -*-

from django import forms

from ..models import Expense, ExpenseType, Store

# # -----------------------------------------------------------------------------
# # Users
# # -----------------------------------------------------------------------------


class MyExpenseTypeForm(forms.ModelForm):
    """Custom UserCreationForm."""

    class Meta:
        model = ExpenseType
        fields = [
            "name",
            "is_active",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].required = True


class MyExpenseForm(forms.ModelForm):
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["type"].queryset = ExpenseType.objects.filter(is_active=True)
        self.fields["store"].queryset = Store.objects.filter(is_active=True)
        for field in self.fields:
            self.fields[field].required = True
