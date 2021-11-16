# -*- coding: utf-8 -*-
from django.urls import include, path

from .. import views
from .auth import urlpatterns as auth_urls
from core.customer import views as customer_views
from core.store_manager import views as store_manager_views
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
]
