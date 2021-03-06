# # -*- coding: utf-8 -*-

import datetime
from django import forms
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

    def save(self, commit=True):
        instance = super().save(commit=False)

        if commit:
            # days = instance.plan.days + instance.plan.months * 30
            # instance.start_date = datetime.datetime.now
            # instance.end_date = datetime.timedelta(days=days)
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
