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
    MyExpenseChangeForm,
    MyExpenseCreationForm,
    MyExpenseTypeChangeForm,
    MyExpenseTypeCreationForm,
)
from ..models import Expense, ExpenseType

# -----------------------------------------------------------------------------
# Users
# -----------------------------------------------------------------------------


class ExpenseListView(MyListView):
    # paginate_by = 25
    model = Expense
    queryset = model.objects.all()
    template_name = "customadmin/expenses/expense_list.html"
    permission_required = ("expenses.view_expense",)


class ExpenseCreateView(MyCreateView):
    model = Expense
    form_class = MyExpenseCreationForm
    template_name = "customadmin/expenses/expense_form.html"
    permission_required = ("expenses.add_expense",)


class ExpenseUpdateView(MyUpdateView):
    model = Expense
    form_class = MyExpenseChangeForm
    template_name = "customadmin/expenses/expense_form.html"
    permission_required = ("expenses.change_expense",)


class ExpenseDeleteView(MyDeleteView):
    model = Expense
    template_name = "customadmin/confirm_delete.html"
    permission_required = ("expenses.delete_expense",)


class ExpenseAjaxPagination(DataTableMixin, HasPermissionsMixin, MyLoginRequiredView):
    """Built this before realizing there is
    https://bitbucket.org/pigletto/django-datatables-view."""

    model = Expense
    queryset = Expense.objects.all().order_by("-created_at")

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
                # Q(username__icontains=self.search)
                # | Q(first_name__icontains=self.search)
                # | Q(last_name__icontains=self.search)
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
                    # "modified": o.modified.strftime("%b. %d, %Y, %I:%M %p"),
                    # "actions": self._get_actions(o),
                }
            )
        return data


# -----------------------------------------------------------------------------
# Users
# -----------------------------------------------------------------------------


class ExpenseTypeListView(MyListView):
    # paginate_by = 25
    model = ExpenseType
    queryset = model.objects.all()
    template_name = "customadmin/expense-types/expensetype_list.html"
    permission_required = ("expensetypes.view_expensetype",)


class ExpenseTypeCreateView(MyCreateView):
    model = ExpenseType
    form_class = MyExpenseTypeCreationForm
    template_name = "customadmin/expense-types/expensetype_form.html"
    permission_required = ("expensetypes.add_expensetype",)


class ExpenseTypeUpdateView(MyUpdateView):
    model = ExpenseType
    form_class = MyExpenseTypeChangeForm
    template_name = "customadmin/expense-types/expensetype_form.html"
    permission_required = ("expensetypes.change_expensetype",)


class ExpenseTypeDeleteView(MyDeleteView):
    model = ExpenseType
    template_name = "customadmin/confirm_delete.html"
    permission_required = ("expensetypes.delete_expensetype",)


class ExpenseTypeAjaxPagination(
    DataTableMixin, HasPermissionsMixin, MyLoginRequiredView
):
    """Built this before realizing there is
    https://bitbucket.org/pigletto/django-datatables-view."""

    model = ExpenseType
    queryset = ExpenseType.objects.all().order_by("-created_at")

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
                # Q(username__icontains=self.search)
                # | Q(first_name__icontains=self.search)
                # | Q(last_name__icontains=self.search)
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
                    # "modified": o.modified.strftime("%b. %d, %Y, %I:%M %p"),
                    # "actions": self._get_actions(o),
                }
            )
        return data
