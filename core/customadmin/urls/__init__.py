# -*- coding: utf-8 -*-
from core.customer import views as customer_views
from core.delivery_agent import views as delivery_agent_views
from core.store_manager import views as store_manager_views
from django.urls import include, path

from .. import views
from .auth import urlpatterns as auth_urls
from .groups import urlpatterns as group_urls

# -----------------------------------------------------------------------------

app_name = "customadmin"

urlpatterns = [
    path("groups/", include((group_urls, "auth"))),
    path("", views.IndexView.as_view(), name="index"),
    # Auth URLs
    path("", include(auth_urls)),
    # ----------------------------------------------------------------------------------
    # User
    path("users/", views.UserListView.as_view(), name="user-list"),
    path("users/create/", views.UserCreateView.as_view(), name="user-create"),
    path("users/<int:pk>/update/", views.UserUpdateView.as_view(), name="user-update"),
    path("users/<int:pk>/profile/update/", views.UserProfileUpdateView.as_view(), name="user-profile-update"),
    path("users/<int:pk>/delete/", views.UserDeleteView.as_view(), name="user-delete"),
    path(
        "users/<int:pk>/password/",
        views.UserPasswordView.as_view(),
        name="user-password",
    ),
    path("users/ajax-users", views.UserAjaxPagination.as_view(), name="user-list-ajax"),
    # ----------------------------------------------------------------------------------
    # Customer
    path("customers/", customer_views.CustomerListView.as_view(), name="customer-list"),
    path(
        "customers/create/",
        customer_views.CustomerCreateView.as_view(),
        name="customer-create",
    ),
    path(
        "customers/<int:pk>/update/",
        customer_views.CustomerUpdateView.as_view(),
        name="customer-update",
    ),
    path(
        "customers/<int:pk>/delete/",
        customer_views.CustomerDeleteView.as_view(),
        name="customer-delete",
    ),
    path(
        "customers/ajax-customers",
        customer_views.CustomerAjaxPagination.as_view(),
        name="customer-list-ajax",
    ),
    path(
        "customers/change-status/",
        customer_views.CustomerChangeStatus.as_view(),
        name="customer-change-status",
    ),
    # ----------------------------------------------------------------------------------
    # Membership
    path(
        "memberships/",
        customer_views.MembershipListView.as_view(),
        name="membership-list",
    ),
    path(
        "memberships/create/",
        customer_views.MembershipCreateView.as_view(),
        name="membership-create",
    ),
    path(
        "memberships/<int:pk>/update/",
        customer_views.MembershipUpdateView.as_view(),
        name="membership-update",
    ),
    path(
        "memberships/<int:pk>/delete/",
        customer_views.MembershipDeleteView.as_view(),
        name="membership-delete",
    ),
    path(
        "memberships/ajax-Memberships",
        customer_views.MembershipAjaxPagination.as_view(),
        name="membership-list-ajax",
    ),
    # ----------------------------------------------------------------------------------
    # deliveryboys
    path(
        "delivery-boys/",
        delivery_agent_views.DeliveryBoyListView.as_view(),
        name="deliveryboy-list",
    ),
    path(
        "delivery-boys/create/",
        delivery_agent_views.DeliveryBoyCreateView.as_view(),
        name="deliveryboy-create",
    ),
    path(
        "delivery-boys/<int:pk>/update/",
        delivery_agent_views.DeliveryBoyUpdateView.as_view(),
        name="deliveryboy-update",
    ),
    path(
        "delivery-boys/<int:pk>/delete/",
        delivery_agent_views.DeliveryBoyDeleteView.as_view(),
        name="deliveryboy-delete",
    ),
    path(
        "delivery-boys/ajax-Memberships",
        delivery_agent_views.DeliveryBoyAjaxPagination.as_view(),
        name="deliveryboy-list-ajax",
    ),
    path(
        "delivery-boys/change-status/",
        delivery_agent_views.DeliveryBoyChangeStatus.as_view(),
        name="deliveryboy-change-status",
    ),
    # ----------------------------------------------------------------------------------
    # Store
    path("stores/", store_manager_views.StoreListView.as_view(), name="store-list"),
    path(
        "stores/create/",
        store_manager_views.StoreCreateView.as_view(),
        name="store-create",
    ),
    path(
        "stores/<int:pk>/update/",
        store_manager_views.StoreUpdateView.as_view(),
        name="store-update",
    ),
    path(
        "stores/<int:pk>/delete/",
        store_manager_views.StoreDeleteView.as_view(),
        name="store-delete",
    ),
    path(
        "stores/ajax-stores",
        store_manager_views.StoreAjaxPagination.as_view(),
        name="store-list-ajax",
    ),
    # ----------------------------------------------------------------------------------
    # Store
    path(
        "categories/",
        store_manager_views.CategoryListView.as_view(),
        name="category-list",
    ),
    path(
        "categories/create/",
        store_manager_views.CategoryCreateView.as_view(),
        name="category-create",
    ),
    path(
        "categories/<int:pk>/update/",
        store_manager_views.CategoryUpdateView.as_view(),
        name="category-update",
    ),
    path(
        "categories/<int:pk>/delete/",
        store_manager_views.CategoryDeleteView.as_view(),
        name="category-delete",
    ),
    path(
        "categories/ajax-stores",
        store_manager_views.CategoryAjaxPagination.as_view(),
        name="category-list-ajax",
    ),
    # ----------------------------------------------------------------------------------
    # Store
    path(
        "sub-categories/",
        store_manager_views.SubCategoryListView.as_view(),
        name="subcategory-list",
    ),
    path(
        "sub-categories/create/",
        store_manager_views.SubCategoryCreateView.as_view(),
        name="subcategory-create",
    ),
    path(
        "sub-categories/<int:pk>/update/",
        store_manager_views.SubCategoryUpdateView.as_view(),
        name="subcategory-update",
    ),
    path(
        "sub-categories/<int:pk>/delete/",
        store_manager_views.SubCategoryDeleteView.as_view(),
        name="subcategory-delete",
    ),
    path(
        "sub-categories/ajax-stores",
        store_manager_views.SubCategoryAjaxPagination.as_view(),
        name="subcategory-list-ajax",
    ),
    # ----------------------------------------------------------------------------------
    # Store
    path(
        "delivery-charges/",
        store_manager_views.DeliveryChargeListView.as_view(),
        name="deliverycharge-list",
    ),
    path(
        "delivery-charges/create/",
        store_manager_views.DeliveryChargeCreateView.as_view(),
        name="deliverycharge-create",
    ),
    path(
        "delivery-charges/<int:pk>/update/",
        store_manager_views.DeliveryChargeUpdateView.as_view(),
        name="deliverycharge-update",
    ),
    path(
        "delivery-charges/<int:pk>/delete/",
        store_manager_views.DeliveryChargeDeleteView.as_view(),
        name="deliverycharge-delete",
    ),
    path(
        "delivery-charges/ajax-stores",
        store_manager_views.DeliveryChargeAjaxPagination.as_view(),
        name="deliverycharge-list-ajax",
    ),
    # ----------------------------------------------------------------------------------
    # Store
    path(
        "coupons/",
        store_manager_views.CouponListView.as_view(),
        name="coupon-list",
    ),
    path(
        "coupons/create/",
        store_manager_views.CouponCreateView.as_view(),
        name="coupon-create",
    ),
    path(
        "coupons/<int:pk>/update/",
        store_manager_views.CouponUpdateView.as_view(),
        name="coupon-update",
    ),
    path(
        "coupons/<int:pk>/delete/",
        store_manager_views.CouponDeleteView.as_view(),
        name="coupon-delete",
    ),
    path(
        "coupons/ajax-stores",
        store_manager_views.CouponAjaxPagination.as_view(),
        name="coupon-list-ajax",
    ),
    # ----------------------------------------------------------------------------------
    # Store
    path(
        "expenses/",
        store_manager_views.ExpenseListView.as_view(),
        name="expense-list",
    ),
    path(
        "expenses/create/",
        store_manager_views.ExpenseCreateView.as_view(),
        name="expense-create",
    ),
    path(
        "expenses/<int:pk>/update/",
        store_manager_views.ExpenseUpdateView.as_view(),
        name="expense-update",
    ),
    path(
        "expenses/<int:pk>/delete/",
        store_manager_views.ExpenseDeleteView.as_view(),
        name="expense-delete",
    ),
    path(
        "expenses/ajax-stores",
        store_manager_views.ExpenseAjaxPagination.as_view(),
        name="expense-list-ajax",
    ),
    # ----------------------------------------------------------------------------------
    # Store
    path(
        "expense-types/",
        store_manager_views.ExpenseTypeListView.as_view(),
        name="expensetype-list",
    ),
    path(
        "expense-types/create/",
        store_manager_views.ExpenseTypeCreateView.as_view(),
        name="expensetype-create",
    ),
    path(
        "expense-types/<int:pk>/update/",
        store_manager_views.ExpenseTypeUpdateView.as_view(),
        name="expensetype-update",
    ),
    path(
        "expense-types/<int:pk>/delete/",
        store_manager_views.ExpenseTypeDeleteView.as_view(),
        name="expensetype-delete",
    ),
    path(
        "expense-types/ajax-stores",
        store_manager_views.ExpenseTypeAjaxPagination.as_view(),
        name="expensetype-list-ajax",
    ),
    # ----------------------------------------------------------------------------------
    # Store
    path(
        "plans/",
        store_manager_views.PlanListView.as_view(),
        name="plan-list",
    ),
    path(
        "plans/create/",
        store_manager_views.PlanCreateView.as_view(),
        name="plan-create",
    ),
    path(
        "plans/<int:pk>/update/",
        store_manager_views.PlanUpdateView.as_view(),
        name="plan-update",
    ),
    path(
        "plans/<int:pk>/delete/",
        store_manager_views.PlanDeleteView.as_view(),
        name="plan-delete",
    ),
    path(
        "plans/ajax-stores",
        store_manager_views.PlanAjaxPagination.as_view(),
        name="plan-list-ajax",
    ),
    # ----------------------------------------------------------------------------------
    # Store
    path(
        "products/",
        store_manager_views.ProductListView.as_view(),
        name="product-list",
    ),
    path(
        "products/create/",
        store_manager_views.ProductCreateView.as_view(),
        name="product-create",
    ),
    path(
        "products/<int:pk>/update/",
        store_manager_views.ProductUpdateView.as_view(),
        name="product-update",
    ),
    path(
        "products/<int:pk>/delete/",
        store_manager_views.ProductDeleteView.as_view(),
        name="product-delete",
    ),
    path(
        "products/ajax-stores",
        store_manager_views.ProductAjaxPagination.as_view(),
        name="product-list-ajax",
    ),
]
