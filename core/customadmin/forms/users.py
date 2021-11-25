# # -*- coding: utf-8 -*-

from django import forms
from django.conf import settings

# from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import Group, Permission
from core.user.models import User

# # -----------------------------------------------------------------------------
# # Util methods
# # -----------------------------------------------------------------------------


def filter_perms():
    """Remove permissions we don't need to worry about managing."""
    return Permission.objects.exclude(
        content_type_id__app_label__in=settings.ADMIN_HIDE_PERMS
    )


# # -----------------------------------------------------------------------------
# # Users
# # -----------------------------------------------------------------------------


class MyUserCreationForm(UserCreationForm):
    """Custom UserCreationForm."""

    class Meta(UserCreationForm.Meta):
        model = User
        fields = [
            "password1",
            "email",
            "username",
            "first_name",
            "last_name",
            "role",
            "is_manager",
            "is_staff",
            "is_active",
            "is_superuser",
            "groups",
            "user_permissions",
            "profile_image",
            "description",
            "address",
            "city",
            "state",
            "country",
            "pincode",
        ]

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        # filter out the permissions we don't want the user to see
        for field in ["username", "email", "role"]:
            self.fields[field].required = True

    def save(self, commit=True):
        instance = super().save(commit=False)

        if commit:
            instance.save()

            # UserCreationForm does NOT save groups or user_permissions
            # by default so we add back that functionality here
            for g in self.cleaned_data["groups"]:
                instance.groups.add(g)

        return instance


class MyUserChangeForm(UserChangeForm):
    """Custom UserChangeForm."""

    class Meta(UserChangeForm.Meta):
        model = User

    def __init__(self, user, *args, **kwargs):
        # self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)
        self.user = user

        for field in ["username", "email", "role"]:
            self.fields[field].required = True


class MyUserProfileChangeForm(UserChangeForm):
    """Custom UserCreationForm."""

    class Meta(UserChangeForm.Meta):
        model = User
        fields = [
            "email",
            "username",
            "first_name",
            "last_name",
            "profile_image",
            "description",
            "address",
            "city",
            "state",
            "country",
            "pincode",
        ]

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        # filter out the permissions we don't want the user to see
        for field in [
            "username",
            "email",
        ]:
            self.fields[field].required = True

    def save(self, commit=True):
        instance = super().save(commit=False)

        if commit:
            instance.save()
        return instance


# # -----------------------------------------------------------------------------
# # Groups
# # -----------------------------------------------------------------------------


class MyGroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ["name", "permissions"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # filter out the permissions we don't want the user to see
        self.fields["permissions"].queryset = filter_perms()
