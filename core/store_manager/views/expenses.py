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
    MyExpenseForm,
    MyExpenseTypeForm,
)
from ..models import Expense, ExpenseType

# -----------------------------------------------------------------------------
# Users
# -----------------------------------------------------------------------------


class ExpenseListView(MyListView):
    # paginate_by = 25
    model = Expense
    queryset = model.objects.none()
    template_name = "customadmin/expenses/expense_list.html"
    permission_required = ("store_manager.view_expense",)


class ExpenseCreateView(MyCreateView):
    model = Expense
    form_class = MyExpenseForm
    template_name = "customadmin/expenses/expense_form.html"
    permission_required = ("store_manager.add_expense",)


class ExpenseUpdateView(MyUpdateView):
    model = Expense
    form_class = MyExpenseForm
    template_name = "customadmin/expenses/expense_form.html"
    permission_required = ("store_manager.change_expense",)


class ExpenseDeleteView(MyDeleteView):
    model = Expense
    template_name = "customadmin/confirm_delete.html"
    permission_required = ("store_manager.delete_expense",)


class ExpenseAjaxPagination(DataTableMixin, HasPermissionsMixin, MyLoginRequiredView):
    """Built this before realizing there is
    https://bitbucket.org/pigletto/django-datatables-view."""

    model = Expense
    queryset = Expense.objects.all().order_by("-created_at")

    def _get_actions(self, obj, **kwargs):
        """Get actions column markup."""
        # ctx = super().get_context_data(**kwargs)
        t = get_template("customadmin/partials/list_basic_actions.html")
        can_update = (
            True
            if "store_manager.change_expense"
            in self.request.user.get_group_permissions()
            else False
        )
        can_delete = (
            True
            if "store_manager.delete_expense"
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
                Q(type__name__icontains=self.search)
                | Q(store__name__icontains=self.search)
            )
        return qs

    def prepare_results(self, qs):
        # Create row data for datatables
        data = []
        for o in qs:
            data.append(
                {
                    "type": o.type.name,
                    "store": o.store.name,
                    "amount": o.amount,
                    "actions": self._get_actions(o),
                }
            )
        return data


# -----------------------------------------------------------------------------
# Users
# -----------------------------------------------------------------------------


class ExpenseTypeListView(MyListView):
    # paginate_by = 25
    model = ExpenseType
    queryset = model.objects.none()
    template_name = "customadmin/expense-types/expensetype_list.html"
    permission_required = ("store_manager.view_expensetype",)


class ExpenseTypeCreateView(MyCreateView):
    model = ExpenseType
    form_class = MyExpenseTypeForm
    template_name = "customadmin/expense-types/expensetype_form.html"
    permission_required = ("store_manager.add_expensetype",)


class ExpenseTypeUpdateView(MyUpdateView):
    model = ExpenseType
    form_class = MyExpenseTypeForm
    template_name = "customadmin/expense-types/expensetype_form.html"
    permission_required = ("store_manager.change_expensetype",)


class ExpenseTypeDeleteView(MyDeleteView):
    model = ExpenseType
    template_name = "customadmin/confirm_delete.html"
    permission_required = ("store_manager.delete_expensetype",)


class ExpenseTypeAjaxPagination(
    DataTableMixin, HasPermissionsMixin, MyLoginRequiredView
):
    """Built this before realizing there is
    https://bitbucket.org/pigletto/django-datatables-view."""

    model = ExpenseType
    queryset = ExpenseType.objects.all().order_by("-created_at")

    def _get_actions(self, obj, **kwargs):
        """Get actions column markup."""
        # ctx = super().get_context_data(**kwargs)
        t = get_template("customadmin/partials/list_basic_actions.html")
        can_update = (
            True
            if "store_manager.change_expensetype"
            in self.request.user.get_group_permissions()
            else False
        )
        can_delete = (
            True
            if "store_manager.delete_expensetype"
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
            return qs.filter(Q(name__icontains=self.search))
        return qs

    def prepare_results(self, qs):
        # Create row data for datatables
        data = []
        for o in qs:
            data.append(
                {
                    "name": o.name,
                    "status": o.is_active,
                    "actions": self._get_actions(o),
                }
            )
        return data
