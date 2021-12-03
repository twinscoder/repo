# -*- coding: utf-8 -*-

from django.urls import path

from . import views

# -----------------------------------------------------------------------------

app_name = "auth"

urlpatterns = [
    # Group
    path("", views.GroupListView.as_view(), name="group-list"),
    path("create/", views.GroupCreateView.as_view(), name="group-create"),
    path("<int:pk>/update/", views.GroupUpdateView.as_view(), name="group-update"),
    path("<int:pk>/delete/", views.GroupDeleteView.as_view(), name="group-delete"),
    path("ajax-groups", views.GroupAjaxPagination.as_view(), name="group-list-ajax"),
]

# -----------------------------------------------------------------------------
