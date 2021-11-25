# -*- coding: utf-8 -*-
from django.contrib import messages
from django.db.models import Q
from django.http.response import HttpResponseRedirect
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
from django.urls import reverse
from ..forms import MyCustomerChangeForm, MyCustomerCreationForm
from ..models import Customer, CustomerStatusHistory

# -----------------------------------------------------------------------------
# Users
# -----------------------------------------------------------------------------


class CustomerChangeStatus(MyView):
    permission_required = ("customer.change_customer",)

    def post(self, request, *args, **kwargs):
        customer_id = request.POST.get("customer_id")
        reason = request.POST.get("reason")
        if customer_id and reason:
            instance = Customer.objects.get(id=customer_id)
            instance.is_active = not instance.is_active
            instance.save()
            status_obj = CustomerStatusHistory()
            status_obj.customer = instance
            status_obj.status = instance.is_active
            status_obj.reason = "{0} : By - {1}".format(reason, request.user.username)
            status_obj.save()
            messages.success(request, "Status updated successfully.")
        return HttpResponseRedirect(reverse("customadmin:customer-list"))


class CustomerListView(MyListView):
    # paginate_by = 25
    ordering = ["username"]
    model = Customer
    queryset = model.objects.all()
    template_name = "customadmin/customers/customer_list.html"
    permission_required = ("customer.view_customer",)


class CustomerCreateView(MyCreateView):
    model = Customer
    form_class = MyCustomerCreationForm
    template_name = "customadmin/customers/customer_form.html"
    permission_required = ("customer.add_customer",)


class CustomerUpdateView(MyUpdateView):
    model = Customer
    form_class = MyCustomerChangeForm
    template_name = "customadmin/customers/customer_form.html"
    permission_required = ("customer.change_customer",)


class CustomerDeleteView(MyDeleteView):
    model = Customer
    template_name = "customadmin/confirm_delete.html"
    permission_required = ("customer.delete_customer",)


class CustomerAjaxPagination(DataTableMixin, HasPermissionsMixin, MyLoginRequiredView):
    """Built this before realizing there is
    https://bitbucket.org/pigletto/django-datatables-view."""

    model = Customer
    queryset = Customer.objects.all().order_by("-created_at")

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
                    "username": o.username,
                    "first_name": o.first_name,
                    "last_name": o.last_name,
                    "is_superuser": self._get_is_superuser(o),
                    # "modified": o.modified.strftime("%b. %d, %Y, %I:%M %p"),
                    "actions": self._get_actions(o),
                }
            )
        return data
