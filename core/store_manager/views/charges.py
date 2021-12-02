# -*- coding: utf-8 -*-
from django.contrib.auth.forms import AdminPasswordChangeForm
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
    MyDeliveryChargeForm,
)
from ..models import DeliveryCharge

# -----------------------------------------------------------------------------
# Users
# -----------------------------------------------------------------------------


class DeliveryChargeListView(MyListView):
    # paginate_by = 25
    model = DeliveryCharge
    queryset = model.objects.all()
    template_name = "customadmin/delivery-charges/deliverycharge_list.html"
    permission_required = ("store_manager.view_deliverycharge",)


class DeliveryChargeCreateView(MyCreateView):
    model = DeliveryCharge
    form_class = MyDeliveryChargeForm
    template_name = "customadmin/delivery-charges/deliverycharge_form.html"
    permission_required = ("store_manager.add_deliverycharge",)


class DeliveryChargeUpdateView(MyUpdateView):
    model = DeliveryCharge
    form_class = MyDeliveryChargeForm
    template_name = "customadmin/delivery-charges/deliverycharge_form.html"
    permission_required = ("store_manager.change_deliverycharge",)


class DeliveryChargeDeleteView(MyDeleteView):
    model = DeliveryCharge
    template_name = "customadmin/confirm_delete.html"
    permission_required = ("store_manager.delete_deliverycharge",)


class DeliveryChargeAjaxPagination(
    DataTableMixin, HasPermissionsMixin, MyLoginRequiredView
):
    """Built this before realizing there is
    https://bitbucket.org/pigletto/django-datatables-view."""

    model = DeliveryCharge
    queryset = DeliveryCharge.objects.all().order_by("-created_at")

    def _get_actions(self, obj, **kwargs):
        """Get actions column markup."""
        # ctx = super().get_context_data(**kwargs)
        t = get_template("customadmin/partials/list_basic_actions.html")
        can_update = (
            True
            if "store_manager.change_deliverycharge"
            in self.request.user.get_group_permissions()
            else False
        )
        can_delete = (
            True
            if "store_manager.delete_deliverycharge"
            in self.request.user.get_group_permissions()
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
                Q(min_amount__icontains=self.search)
                | Q(max_amount__icontains=self.search)
                | Q(charge_amount__icontains=self.search)
            )
        return qs

    def prepare_results(self, qs):
        # Create row data for datatables
        data = []
        for o in qs:
            data.append(
                {
                    "min_amount": o.min_amount,
                    "max_amount": o.max_amount,
                    "charge_amount": o.charge_amount,
                    "actions": self._get_actions(o),
                }
            )
        return data
