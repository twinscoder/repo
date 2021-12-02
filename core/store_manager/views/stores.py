# -*- coding: utf-8 -*-
from django.db.models import Q
from django.template.loader import get_template
from django_datatables_too.mixins import DataTableMixin

from core.customadmin.mixins import HasPermissionsMixin
from core.customadmin.views.generic import (
    MyCreateView,
    MyDeleteView,
    MyListView,
    MyLoginRequiredView,
    MyUpdateView,
)

from ..forms import MyStoreChangeForm, MyStoreCreationForm
from ..models import Store

# -----------------------------------------------------------------------------
# Users
# -----------------------------------------------------------------------------


class StoreListView(MyListView):
    # paginate_by = 25
    ordering = ["name"]
    model = Store
    queryset = model.objects.none()
    template_name = "customadmin/stores/store_list.html"
    permission_required = ("store_manager.view_store",)


class StoreCreateView(MyCreateView):
    model = Store
    form_class = MyStoreCreationForm
    template_name = "customadmin/stores/store_form.html"
    permission_required = ("store_manager.add_store",)


class StoreUpdateView(MyUpdateView):
    model = Store
    form_class = MyStoreChangeForm
    template_name = "customadmin/stores/store_form.html"
    permission_required = ("store_manager.change_store",)


class StoreDeleteView(MyDeleteView):
    model = Store
    template_name = "customadmin/confirm_delete.html"
    permission_required = ("store_manager.delete_store",)


class StoreAjaxPagination(DataTableMixin, HasPermissionsMixin, MyLoginRequiredView):
    """Built this before realizing there is
    https://bitbucket.org/pigletto/django-datatables-view."""

    model = Store
    queryset = Store.objects.all().order_by("name")

    def _get_actions(self, obj, **kwargs):
        """Get actions column markup."""
        t = get_template("customadmin/partials/list_basic_actions.html")
        can_update = (
            True
            if "store_manager.change_store" in self.request.user.get_group_permissions()
            else False
        )
        can_delete = (
            True
            if "store_manager.delete_store" in self.request.user.get_group_permissions()
            else False
        )
        return t.render(
            {
                "obj": obj,
                "opts": self.model._meta,
                "can_update": can_update,
                "can_delete": can_delete,
            }
        )

    def filter_queryset(self, qs):
        """Return the list of items for this view."""
        # If a search term, filter the query
        if self.search:
            return qs.filter(
                Q(name__icontains=self.search) | Q(phone__icontains=self.search)
            )
        return qs

    def prepare_results(self, qs):
        # Create row data for datatables
        data = []
        for o in qs:
            data.append(
                {
                    "name": o.name,
                    "phone": o.phone,
                    "actions": self._get_actions(o),
                }
            )
        return data
