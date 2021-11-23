import uuid

from config.models import ActivityTracking
from django.db import models
from django.utils.translation import gettext as _
from core.user.models import User

# Create your models here.
class StoreManager(User, ActivityTracking):
    GENDER_CHOICES = (("Male", "MALE"), ("Female", "FEMALE"))
    gender = models.CharField(
        choices=GENDER_CHOICES, max_length=40, blank=True, verbose_name=_("Gender")
    )

    def __str__(self):
        return self.username

    def get_full_name(self):
        return " ".join([self.first_name, self.last_name])

    def get_short_name(self):
        return self.first_name

    class Meta:
        verbose_name = "Store Manager"
        verbose_name_plural = "store managers"
        ordering = ["-created_at"]


class StoreManagerStatusHistory(ActivityTracking):

    store_manager = models.ForeignKey(
        "StoreManager",
        on_delete=models.CASCADE,
        blank=True,
        verbose_name=_("Store Manager"),
    )
    status = models.BooleanField(default=False, verbose_name=_("Status"))
    reason = models.CharField(max_length=255, blank=True, verbose_name=_("Reason"))

    def __unicode__(self):
        return self.store_manager.username

    class Meta:
        verbose_name = "StoreManager Status History"
        verbose_name_plural = "StoreManagers status history"
        ordering = ["-created_at"]
