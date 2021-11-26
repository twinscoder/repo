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
from ..forms import MyCustomerChangeForm, MyCustomerCreationForm, MyCustomerAddressForm
from ..models import Customer, CustomerStatusHistory, CustomerAddress

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
            return qs.filter(Q(username__icontains=self.search))
        return qs

    def prepare_results(self, qs):
        # Create row data for datatables
        data = []
        for o in qs:
            data.append(
                {
                    "username": o.username,
                }
            )
        return data


# ---------------------------------------------------------------------------------
# customer address
# ---------------------------------------------------------------------------------
class CustomerAddressListView(MyListView):
    # paginate_by = 25
    ordering = ["-created_at"]
    model = CustomerAddress
    queryset = model.objects.all()
    template_name = "customadmin/customer-addresses/customeraddress_list.html"
    permission_required = ("customer.view_customeraddress",)


class CustomerAddressCreateView(MyCreateView):
    model = CustomerAddress
    form_class = MyCustomerAddressForm
    template_name = "customadmin/customer-addresses/customeraddress_form.html"
    permission_required = ("customer.add_customeraddress",)


class CustomerAddressUpdateView(MyUpdateView):
    model = CustomerAddress
    form_class = MyCustomerAddressForm
    template_name = "customadmin/customer-addresses/customeraddress_form.html"
    permission_required = ("customer.change_customeraddress",)


class CustomerAddressDeleteView(MyDeleteView):
    model = CustomerAddress
    template_name = "customadmin/confirm_delete.html"
    permission_required = ("customer.delete_customeraddress",)


class CustomerAddressAjaxPagination(
    DataTableMixin, HasPermissionsMixin, MyLoginRequiredView
):
    """Built this before realizing there is
    https://bitbucket.org/pigletto/django-datatables-view."""

    model = CustomerAddress
    queryset = CustomerAddress.objects.all().order_by("-created_at")

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
            data.append({})
        return data
