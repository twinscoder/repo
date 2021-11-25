import uuid

from config.models import ActivityTracking
from django.db import models
from django.utils.translation import gettext as _


# Create your models here.
class DeliveryBoyWallet(ActivityTracking):

    delivery_boy = models.ForeignKey(
        "DeliveryBoy",
        on_delete=models.CASCADE,
        blank=True,
        verbose_name=_("Delivery Boy"),
    )
    amount = models.FloatField(default=0, blank=True, verbose_name=_("Amount"))

    unique_id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        verbose_name=_("Unique Id"),
    )
    is_active = models.BooleanField(default=True, verbose_name=_("Status"))

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "Delivery Boy Wallet"
        verbose_name_plural = "delivery boy wallet"
        ordering = ["-created_at"]


# Create your models here.
class DeliveryBoyWalletHistory(ActivityTracking):

    PAYMENT_TYPES_CHOICES = (
        (("Credit"), ("Credit")),
        (("Debit"), ("Debit")),
        (("Other"), ("Other")),
    )

    wallet = models.ForeignKey(
        "DeliveryBoyWallet",
        on_delete=models.CASCADE,
        blank=True,
        verbose_name=_("Wallet"),
    )
    log = models.CharField(
        max_length=255, default="", blank=True, verbose_name=_("Log")
    )
    amount = models.FloatField(default=0, blank=True, verbose_name=_("Amount"))
    payment_type = models.CharField(
        choices=PAYMENT_TYPES_CHOICES,
        max_length=255,
        default="",
        blank=True,
        verbose_name=_("Payment Type"),
    )

    unique_id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        verbose_name=_("Unique Id"),
    )
    is_active = models.BooleanField(default=True, verbose_name=_("Status"))

    def __str__(self):
        return self.wallet.delivery_boy.username

    class Meta:
        verbose_name = "Delivery Boy Wallet History"
        verbose_name_plural = "delivery boy wallet history"
        ordering = ["-created_at"]
