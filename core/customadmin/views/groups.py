# -*- coding: utf-8 -*-
from django.db.models.query_utils import Q
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
from django.contrib.auth.models import Group

from ..forms import MyGroupForm

# -----------------------------------------------------------------------------
# Groups
# -----------------------------------------------------------------------------


class GroupListView(MyListView):
    # paginate_by = 25
    model = Group
    queryset = model.objects.none()
    template_name = "customadmin/adminuser/group_list.html"
    permission_required = ("auth.view_group",)


class GroupCreateView(MyCreateView):
    model = Group
    form_class = MyGroupForm
    template_name = "customadmin/adminuser/group_form.html"
    permission_required = ("auth.add_group",)


class GroupUpdateView(MyUpdateView):
    model = Group
    form_class = MyGroupForm
    template_name = "customadmin/adminuser/group_form.html"
    permission_required = ("auth.change_group",)


class GroupDeleteView(MyDeleteView):
    model = Group
    template_name = "customadmin/confirm_delete.html"
    permission_required = ("auth.delete_group",)


class GroupAjaxPagination(DataTableMixin, HasPermissionsMixin, MyLoginRequiredView):
    """Built this before realizing there is
    https://bitbucket.org/pigletto/django-datatables-view."""

    model = Group
    queryset = Group.objects.all()

    def _get_actions(self, obj, **kwargs):
        """Get actions column markup."""
        t = get_template("customadmin/partials/list_basic_actions.html")
        can_update = (
            True
            if "auth.change_group" in self.request.user.get_group_permissions()
            else False
        )
        can_delete = (
            True
            if "auth.delete_group" in self.request.user.get_group_permissions()
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
            return qs.filter(Q(name__icontains=self.search))
        return qs

    def prepare_results(self, qs):
        # Create row data for datatables
        data = []
        for o in qs:
            data.append(
                {
                    "name": o.name,
                    "actions": self._get_actions(o),
                }
            )
        return data
