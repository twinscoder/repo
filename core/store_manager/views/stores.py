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
    # queryset = model.objects.exclude(username="manifestingest")
    template_name = "customadmin/stores/store_list.html"
    permission_required = ("stores.view_store",)


class StoreCreateView(MyCreateView):
    model = Store
    form_class = MyStoreCreationForm
    template_name = "customadmin/stores/store_form.html"
    permission_required = ("stores.add_store",)


class StoreUpdateView(MyUpdateView):
    model = Store
    form_class = MyStoreChangeForm
    template_name = "customadmin/stores/store_form.html"
    permission_required = ("stores.change_store",)


class StoreDeleteView(MyDeleteView):
    model = Store
    template_name = "customadmin/confirm_delete.html"
    permission_required = ("stores.delete_store",)


class StoreAjaxPagination(DataTableMixin, HasPermissionsMixin, MyLoginRequiredView):
    """Built this before realizing there is
    https://bitbucket.org/pigletto/django-datatables-view."""

    model = Store
    queryset = Store.objects.all().order_by("name")

    def _get_is_superuser(self, obj):
        """Get boolean column markup."""
        t = get_template("customadmin/partials/list_boolean.html")
        return t.render({"bool_val": obj.is_superuser})

    def _get_actions(self, obj, **kwargs):
        """Get actions column markup."""
        # ctx = super().get_context_data(**kwargs)
        t = get_template("customadmin/partials/list_basic_actions.html")
        # ctx.update({"obj": obj})
        # print(ctx)
        return t.render({"o": obj})

    def filter_queryset(self, qs):
        """Return the list of items for this view."""
        # If a search term, filter the query
        if self.search:
            return qs.filter()
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
