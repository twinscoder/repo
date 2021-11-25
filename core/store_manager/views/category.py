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
    MyCategoryForm,
    MySubCategoryForm,
)
from ..models import Category, SubCategory

# -----------------------------------------------------------------------------
# Users
# -----------------------------------------------------------------------------


class CategoryListView(MyListView):
    # paginate_by = 25
    model = Category
    queryset = model.objects.all()
    template_name = "customadmin/categories/category_list.html"
    permission_required = ("store_manager.view_category",)


class CategoryCreateView(MyCreateView):
    model = Category
    form_class = MyCategoryForm
    template_name = "customadmin/categories/category_form.html"
    permission_required = ("store_manager.add_category",)


class CategoryUpdateView(MyUpdateView):
    model = Category
    form_class = MyCategoryForm
    template_name = "customadmin/categories/category_form.html"
    permission_required = ("store_manager.change_category",)


class CategoryDeleteView(MyDeleteView):
    model = Category
    template_name = "customadmin/confirm_delete.html"
    permission_required = ("store_manager.delete_category",)


class CategoryAjaxPagination(DataTableMixin, HasPermissionsMixin, MyLoginRequiredView):
    """Built this before realizing there is
    https://bitbucket.org/pigletto/django-datatables-view."""

    model = Category
    queryset = Category.objects.all().order_by("-created_at")

    def _get_actions(self, obj, **kwargs):
        """Get actions column markup."""

        t = get_template("customadmin/partials/list_basic_actions.html")
        return t.render({"obj": obj})

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
                    # "actions": self._get_actions(o),
                }
            )
        return data


# -----------------------------------------------------------------------------
# Users
# -----------------------------------------------------------------------------


class SubCategoryListView(MyListView):
    # paginate_by = 25
    model = SubCategory
    queryset = model.objects.all()
    template_name = "customadmin/subcategories/subcategory_list.html"
    permission_required = ("store_manager.view_subcategory",)


class SubCategoryCreateView(MyCreateView):
    model = SubCategory
    form_class = MySubCategoryForm
    template_name = "customadmin/subcategories/subcategory_form.html"
    permission_required = ("store_manager.add_subcategory",)


class SubCategoryUpdateView(MyUpdateView):
    model = SubCategory
    form_class = MySubCategoryForm
    template_name = "customadmin/subcategories/subcategory_form.html"
    permission_required = ("store_manager.change_subcategory",)


class SubCategoryDeleteView(MyDeleteView):
    model = SubCategory
    template_name = "customadmin/confirm_delete.html"
    permission_required = ("store_manager.delete_subcategory",)


class SubCategoryAjaxPagination(
    DataTableMixin, HasPermissionsMixin, MyLoginRequiredView
):
    """Built this before realizing there is
    https://bitbucket.org/pigletto/django-datatables-view."""

    model = SubCategory
    queryset = SubCategory.objects.all().order_by("-created_at")

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
                    # # "modified": o.modified.strftime("%b. %d, %Y, %I:%M %p"),
                    # "actions": self._get_actions(o),
                }
            )
        return data
