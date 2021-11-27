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

from ..forms import (
    MyOrderCreationForm,
    MyOrderChangeForm,
)
from ..models import Order

# -----------------------------------------------------------------------------
# Users
# -----------------------------------------------------------------------------


class OrderListView(MyListView):
    # paginate_by = 25
    model = Order
    queryset = model.objects.all()
    template_name = "customadmin/orders/order_list.html"
    permission_required = ("store_manager.view_order",)


class OrderCreateView(MyCreateView):
    model = Order
    form_class = MyOrderCreationForm
    template_name = "customadmin/orders/order_form.html"
    permission_required = ("store_manager.add_order",)


class OrderUpdateView(MyUpdateView):
    model = Order
    form_class = MyOrderChangeForm
    template_name = "customadmin/orders/order_form.html"
    permission_required = ("store_manager.change_order",)


class OrderDeleteView(MyDeleteView):
    model = Order
    template_name = "customadmin/confirm_delete.html"
    permission_required = ("store_manager.delete_order",)


class OrderAjaxPagination(DataTableMixin, HasPermissionsMixin, MyLoginRequiredView):
    """Built this before realizing there is
    https://bitbucket.org/pigletto/django-datatables-view."""

    model = Order
    queryset = Order.objects.all().order_by("-created_at")

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
            return qs.filter(
                # Q(username__icontains=self.search
            )
        return qs

    def prepare_results(self, qs):
        # Create row data for datatables
        data = []
        for o in qs:
            data.append(
                {
                    # "username": o.username,
                    # "first_name": o.first_name,
                }
            )
        return data
