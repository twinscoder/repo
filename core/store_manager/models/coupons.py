import uuid

from config.models import ActivityTracking
from django.db import models
from django.utils.translation import gettext as _


# Create your models here.
class Coupon(ActivityTracking):

    DISCOUNT_CHOICES = ((("Fixed", "Fixed")), (("Percentage"), ("Percentage")))

    code = models.CharField(
        max_length=50, blank=True, null=True, default="", verbose_name=_("Cuopon Code")
    )
    amount = models.FloatField(
        max_length=3,
        blank=True,
        null=True,
        default=0,
        verbose_name=_("Amount in Percentage (%)"),
    )
    discount_type = models.CharField(
        choices=DISCOUNT_CHOICES,
        max_length=10,
        blank=True,
        verbose_name=_("Discount Type"),
    )
    is_repeatable = models.BooleanField(default=True, verbose_name=_("Is Repeatable"))
    min_amount = models.FloatField(
        blank=True, null=True, default=0, verbose_name=_("Min Amount")
    )
    max_amount = models.FloatField(
        blank=True, null=True, default=0, verbose_name=_("Max Amount")
    )
    start_date = models.DateTimeField(
        blank=True, null=True, verbose_name=_("Start Date")
    )
    expiry_date = models.DateTimeField(
        blank=True, null=True, verbose_name=_("Expiry Date")
    )
    description = models.CharField(
        max_length=255, blank=True, verbose_name=_("Description")
    )
    count = models.IntegerField(default=0, verbose_name=_("Count"))

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
        verbose_name = "Coupon"
        verbose_name_plural = "coupons"
        ordering = ["-created_at"]
