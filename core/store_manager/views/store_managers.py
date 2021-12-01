# -*- coding: utf-8 -*-
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AdminPasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import JsonResponse
from django.template.loader import get_template
from django_datatables_too.mixins import DataTableMixin

from core.customadmin.mixins import HasPermissionsMixin
from core.customadmin.views.generic import (
    MyCreateView,
    MyDeleteView,
    MyListView,
    MyLoginRequiredView,
    MyUpdateView,
    MyView,
)

from ..forms import MyStoreManagerChangeForm, MyStoreManagerCreationForm
from core.store_manager.models import StoreManager

# -----------------------------------------------------------------------------
# Users
# -----------------------------------------------------------------------------


class StoreManagerListView(MyListView):
    # paginate_by = 25
    ordering = ["username"]
    model = StoreManager
    queryset = model.objects.all()
    template_name = "customadmin/store-manager/storemanager_list.html"
    permission_required = ("storemanagers.view_storemanager",)


class StoreManagerCreateView(MyCreateView):
    model = StoreManager
    form_class = MyStoreManagerCreationForm
    template_name = "customadmin/store-manager/storemanager_form.html"
    permission_required = ("storemanagers.add_storemanager",)


class StoreManagerUpdateView(MyUpdateView):
    model = StoreManager
    form_class = MyStoreManagerChangeForm
    template_name = "customadmin/store-manager/storemanager_form.html"
    permission_required = ("storemanagers.change_storemanager",)


class StoreManagerDeleteView(MyDeleteView):
    model = StoreManager
    template_name = "customadmin/confirm_delete.html"
    permission_required = ("storemanagers.delete_storemanager",)


class StoreManagerPasswordView(MyUpdateView):
    model = StoreManager
    form_class = AdminPasswordChangeForm
    template_name = "customadmin/adminuser/password_change_form.html"
    permission_required = ("users.change_user",)


class StoreManagerAjaxPagination(
    DataTableMixin, HasPermissionsMixin, MyLoginRequiredView
):
    """Built this before realizing there is
    https://bitbucket.org/pigletto/django-datatables-view."""

    model = StoreManager
    queryset = StoreManager.objects.all().order_by("-created_at")

    def _get_is_superuser(self, obj):
        """Get boolean column markup."""
        t = get_template("customadmin/partials/list_boolean.html")
        return t.render({"bool_val": obj.is_superuser})

    def _get_actions(self, obj, **kwargs):
        """Get actions column markup."""
        t = get_template("customadmin/partials/list_basic_actions.html")
        user_perms = {
            "view_perm": True
            if self.request.user.has_perm("%s.%s" % ("core", "view_invite"))
            else False,
            "change_perm": True
            if self.request.user.has_perm("%s.%s" % ("core", "change_invite"))
            else False,
            "delete_perm": True
            if self.request.user.has_perm("%s.%s" % ("core", "delete_invite"))
            else False,
        }
        return t.render({"obj": obj, "user_perms": user_perms})

    def filter_queryset(self, qs):
        """Return the list of items for this view."""
        # If a search term, filter the query
        if self.search:
            return qs.filter(
                Q(username__icontains=self.search)
                | Q(first_name__icontains=self.search)
                | Q(last_name__icontains=self.search)
            )
        return qs

    def prepare_results(self, qs):
        # Create row data for datatables
        data = []
        for o in qs:
            data.append(
                {
                    "username": o.username,
                    "first_name": o.first_name,
                    "last_name": o.last_name,
                    "is_superuser": self._get_is_superuser(o),
                    # "modified": o.modified.strftime("%b. %d, %Y, %I:%M %p"),
                    "actions": self._get_actions(o),
                }
            )
        return data
