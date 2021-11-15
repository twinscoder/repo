# -*- coding: utf-8 -*-

from django.urls import path

from . import views

# -----------------------------------------------------------------------------

app_name = "users"

urlpatterns = [
    # User
    path("", views.UserListView.as_view(), name="user-list"),
    path("create/", views.UserCreateView.as_view(), name="user-create"),
    path("<int:pk>/update/", views.UserUpdateView.as_view(), name="user-update"),
    path("<int:pk>/delete/", views.UserDeleteView.as_view(), name="user-delete"),
    path(
        "<int:pk>/password/",
        views.UserPasswordView.as_view(),
        name="user-password",
    ),
    path("ajax-users", views.UserAjaxPagination.as_view(), name="user-list-ajax"),
]

# -----------------------------------------------------------------------------
