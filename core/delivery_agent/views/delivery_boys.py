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
                Q(username__icontains=self.search)
                | Q(first_name__icontains=self.search)
                | Q(last_name__icontains=self.search)
                # | Q(state__icontains=self.search)
                # | Q(year__icontains=self.search)
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
                    # "last_name": o.last_name,
                    # "is_superuser": self._get_is_superuser(o),
                    # # "modified": o.modified.strftime("%b. %d, %Y, %I:%M %p"),
                    # "actions": self._get_actions(o),
                }
            )
        return data
