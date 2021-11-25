import uuid

from config.models import ActivityTracking
from django.db import models
from django.utils.translation import gettext as _


# Create your models here.
class CustomerWallet(ActivityTracking):

    customer = models.ForeignKey("Customer", on_delete=models.CASCADE, blank=True)
    amount = models.FloatField(default=0, blank=True)

    unique_id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        verbose_name=_("Unique Id"),
    )
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Customer Wallet"
        verbose_name_plural = "customer wallet"
        ordering = ["-created_at"]


# Create your models here.
class CustomerWalletHistory(ActivityTracking):

    CREDIT = "Credit"
    DEBIT = "Debit"
    OTHER = "Other"

    PAYMENT_TYPES_CHOICES = (
        (CREDIT, "Credit"),
        (DEBIT, "Debit"),
        (OTHER, "Other"),
    )

    wallet = models.ForeignKey(
        "CustomerWallet", on_delete=models.CASCADE, blank=True, verbose_name=_("Wallet")
    )
    log = models.CharField(
        max_length=255, default="", blank=True, verbose_name=_("Log")
    )
    amount = models.FloatField(
        default=0, blank=True, verbose_name=_("Amount / Balance")
    )
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
        return self.wallet.customer.username

    class Meta:
        verbose_name = "Customer Wallet History"
        verbose_name_plural = "customer wallet history"
        ordering = ["-created_at"]
