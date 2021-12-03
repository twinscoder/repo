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

from ..forms import MyMembershipChangeForm, MyMembershipCreationForm
from ..models import Membership

# -----------------------------------------------------------------------------
# Users
# -----------------------------------------------------------------------------


class MembershipListView(MyListView):
    # paginate_by = 25
    model = Membership
    queryset = model.objects.none()
    template_name = "customadmin/memberships/membership_list.html"
    permission_required = ("customer.view_membership",)


class MembershipCreateView(MyCreateView):
    model = Membership
    form_class = MyMembershipCreationForm
    template_name = "customadmin/memberships/membership_form.html"
    permission_required = ("customer.add_membership",)


class MembershipUpdateView(MyUpdateView):
    model = Membership
    form_class = MyMembershipChangeForm
    template_name = "customadmin/memberships/membership_form.html"
    permission_required = ("customer.change_membership",)


class MembershipDeleteView(MyDeleteView):
    model = Membership
    template_name = "customadmin/confirm_delete.html"
    permission_required = ("customer.delete_membership",)


class MembershipAjaxPagination(
    DataTableMixin, HasPermissionsMixin, MyLoginRequiredView
):
    """Built this before realizing there is
    https://bitbucket.org/pigletto/django-datatables-view."""

    model = Membership
    queryset = Membership.objects.all().order_by("-created_at")

    def _get_actions(self, obj, **kwargs):
        """Get actions column markup."""
        # ctx = super().get_context_data(**kwargs)
        t = get_template("customadmin/partials/list_basic_actions.html")
        can_update = (
            True
            if "customer.change_membership" in self.request.user.get_group_permissions()
            else False
        )
        can_delete = (
            True
            if "customer.delete_membership" in self.request.user.get_group_permissions()
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
                Q(customer__username__icontains=self.search)
                | Q(plan__name__icontains=self.search)
            )
        return qs

    def prepare_results(self, qs):
        # Create row data for datatables
        data = []
        for o in qs:
            data.append(
                {
                    "customer": o.customer.username,
                    "plan": o.plan.name,
                    "status": o.is_active,
                    "actions": self._get_actions(o),
                }
            )
        return data
