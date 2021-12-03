# -*- coding: utf-8 -*-
from django.contrib.auth.forms import AdminPasswordChangeForm
from django.db.models import Q
from django.http.response import HttpResponseRedirect
from django.template.loader import get_template
from django.urls.base import reverse
from django_datatables_too.mixins import DataTableMixin
from django.contrib import messages
from core.customadmin.mixins import HasPermissionsMixin
from core.customadmin.views.generic import (
    MyCreateView,
    MyDeleteView,
    MyListView,
    MyLoginRequiredView,
    MyUpdateView,
    MyView,
)
from core.delivery_agent.models.delivery_boys import DeliveryBoyStatusHistory

from ..forms import MyDeliveryBoyChangeForm, MyDeliveryBoyCreationForm
from ..models import DeliveryBoy

# -----------------------------------------------------------------------------
# Users
# -----------------------------------------------------------------------------
class DeliveryBoyChangeStatus(MyView):
    permission_required = ("delivery_agent.change_deliveryboy",)

    def post(self, request, *args, **kwargs):
        deliveryboy_id = request.POST.get("deliveryboy_id")
        reason = request.POST.get("reason")
        if deliveryboy_id and reason:
            instance = DeliveryBoy.objects.get(id=deliveryboy_id)
            instance.is_active = not instance.is_active
            instance.save()
            status_obj = DeliveryBoyStatusHistory()
            status_obj.delivery_boy = instance
            status_obj.status = instance.is_active
            status_obj.reason = "{0} : By - {1}".format(reason, request.user.username)
            status_obj.save()
            messages.success(request, "Status updated successfully.")
        return HttpResponseRedirect(reverse("customadmin:deliveryboy-list"))


class DeliveryBoyListView(MyListView):
    # paginate_by = 25
    ordering = ["username"]
    model = DeliveryBoy
    queryset = model.objects.all()
    template_name = "customadmin/delivery-boys/deliveryboy_list.html"
    permission_required = ("delivery_agent.view_deliveryboy",)


class DeliveryBoyCreateView(MyCreateView):
    model = DeliveryBoy
    form_class = MyDeliveryBoyCreationForm
    template_name = "customadmin/delivery-boys/deliveryboy_form.html"
    permission_required = ("delivery_agent.add_deliveryboy",)


class DeliveryBoyUpdateView(MyUpdateView):
    model = DeliveryBoy
    form_class = MyDeliveryBoyChangeForm
    template_name = "customadmin/delivery-boys/deliveryboy_form.html"
    permission_required = ("delivery_agent.change_deliveryboy",)


class DeliveryBoyDeleteView(MyDeleteView):
    model = DeliveryBoy
    template_name = "customadmin/confirm_delete.html"
    permission_required = ("delivery_agent.delete_deliveryboy",)


class DeliveryBoyAjaxPagination(
    DataTableMixin, HasPermissionsMixin, MyLoginRequiredView
):
    """Built this before realizing there is
    https://bitbucket.org/pigletto/django-datatables-view."""

    model = DeliveryBoy
    queryset = DeliveryBoy.objects.all().order_by("-created_at")

    def _get_status(self, obj, **kwargs):
        """Get actions column markup."""
        t = get_template("customadmin/delivery-boys/partials/display_status.html")
        return t.render(
            {
                "obj": obj,
            }
        )

    def _get_actions(self, obj, **kwargs):
        """Get actions column markup."""
        t = get_template("customadmin/partials/list_basic_actions.html")
        can_update = (
            True
            if "delivery_agent.change_deliveryboy"
            in self.request.user.get_group_permissions()
            else False
        )
        can_delete = (
            True
            if "delivery_agent.delete_deliveryboy"
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
            return qs.filter(Q(username__icontains=self.search))
        return qs

    def prepare_results(self, qs):
        # Create row data for datatables
        data = []
        for o in qs:
            data.append(
                {
                    "username": o.username,
                    "status": self._get_status(o),
                    "actions": self._get_actions(o),
                }
            )
        return data
