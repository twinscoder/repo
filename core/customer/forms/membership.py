# # -*- coding: utf-8 -*-

import datetime
from django import forms

from core.customer.models.customers import Customer
from core.store_manager.models.plans import Plan
from ..models import Membership
from core.customadmin.utils import membership_card_generator

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
            "is_active",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["customer"].queryset = Customer.objects.filter(is_active=True)
        self.fields["plan"].queryset = Plan.objects.filter(is_active=True)
        for field in self.fields:
            self.fields[field].required = True

    def save(self, commit=True):
        instance = super().save(commit=False)

        if commit:
            instance.save()
            instance.card_number = membership_card_generator(instance.id)
            instance.save()

        return instance


class MyMembershipChangeForm(forms.ModelForm):
    """Custom UserChangeForm."""

    class Meta:
        model = Membership
        fields = [
            "customer",
            "plan",
            "is_active",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["customer"].queryset = Customer.objects.filter(is_active=True)
        self.fields["plan"].queryset = Plan.objects.filter(is_active=True)
        for field in self.fields:
            self.fields[field].required = True
