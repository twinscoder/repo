# -*- coding: utf-8 -*-

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

# -----------------------------------------------------------------------------


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = "customadmin/index.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        # Stats for dash
        return ctx
