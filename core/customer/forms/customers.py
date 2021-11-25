# # -*- coding: utf-8 -*-
from core.customadmin.utils import refer_code_generator
from django import forms

from ..models import Customer

# # -----------------------------------------------------------------------------
# # Users
# # -----------------------------------------------------------------------------


class MyCustomerCreationForm(forms.ModelForm):
    """Custom UserCreationForm."""

    class Meta:
        model = Customer
        fields = [
            "email",
            "username",
            "first_name",
            "last_name",
            "gender",
            "birth_date",
            "phone",
            "profile_image",
            "description",
            "address",
            "city",
            "state",
            "country",
            "pincode",
            "refer_from",
            "is_active",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in [
            "username",
            "email",
            "first_name",
            "gender",
            "phone",
            "address",
            "city",
            "state",
            "country",
            "pincode",
        ]:
            self.fields[field].required = True

    def save(self, commit=True):
        instance = super().save(commit=False)

        if commit:
            instance.refer_code = refer_code_generator()
            instance.save()

        return instance


class MyCustomerChangeForm(forms.ModelForm):
    """Custom UserChangeForm."""

    class Meta:
        model = Customer
        fields = [
            "email",
            "username",
            "first_name",
            "last_name",
            "gender",
            "birth_date",
            "phone",
            "profile_image",
            "description",
            "address",
            "city",
            "state",
            "country",
            "pincode",
            "refer_from",
            "is_active",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in [
            "username",
            "email",
            "first_name",
            "gender",
            "phone",
            "address",
            "city",
            "state",
            "country",
            "pincode",
        ]:
            self.fields[field].required = True
        self.fields["refer_from"].queryset = Customer.objects.all().exclude(
            pk=self.instance.pk
        )
