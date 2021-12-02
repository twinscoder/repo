import uuid

from config.models import ActivityTracking
from django.db import models
from django.utils.translation import gettext as _


# Create your models here.
class ExpenseType(ActivityTracking):

    name = models.CharField(
        max_length=100, blank=True, null=True, default="", verbose_name=_("Name")
    )

    unique_id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        verbose_name=_("Unique Id"),
    )
    is_active = models.BooleanField(default=True, verbose_name=_("Status"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Expense Type"
        verbose_name_plural = "expense types"
        ordering = ["-created_at"]


# Create your models here.
class Expense(ActivityTracking):

    type = models.ForeignKey(
        "ExpenseType",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name=_("Expense Type"),
    )
    store = models.ForeignKey(
        "Store",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name=_("Store"),
    )
    amount = models.FloatField(
        default=0, blank=True, null=True, verbose_name=_("Amount")
    )
    description = models.CharField(
        max_length=255, default="", blank=True, null=True, verbose_name=_("Description")
    )

    unique_id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        verbose_name=_("Unique Id"),
    )
    is_active = models.BooleanField(default=True, verbose_name=_("Status"))

    def __str__(self):
        return f"{self.type.name} - {self.is_active}"

    class Meta:
        verbose_name = "Expense"
        verbose_name_plural = "expense"
        ordering = ["-created_at"]
