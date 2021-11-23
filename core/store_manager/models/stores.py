import uuid

from config.models import ActivityTracking
from core.delivery_agent.models import DeliveryBoy
from django.db import models
from django.utils.translation import gettext as _
from core.user.models import User

# Create your models here.
class Store(ActivityTracking):

    name = models.CharField(
        max_length=40, blank=True, null=True, default="", verbose_name=_("Name")
    )
    business_email = models.EmailField(
        max_length=100,
        blank=True,
        null=True,
        default="",
        unique=True,
        verbose_name=_("Business Email"),
    )
    phone = models.CharField(max_length=20, blank=True, verbose_name=_("Phone"))
    store_manager = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        related_name="store_manager",
        verbose_name=_("Store Manager"),
    )
    delivery_boys = models.ManyToManyField(
        DeliveryBoy,
        blank=True,
        verbose_name=_("Delivery Boys"),
    )
    image = models.ImageField(
        upload_to="store_image",
        default="sample.jpg",
        null=True,
        blank=True,
        verbose_name=_("Store Image"),
    )
    description = models.CharField(
        max_length=255, blank=True, verbose_name=_("Description")
    )

    address = models.CharField(
        max_length=255, default="", blank=True, verbose_name=_("Address")
    )
    city = models.CharField(max_length=50, blank=True, verbose_name=_("City"))
    state = models.CharField(max_length=50, blank=True, verbose_name=_("State"))
    country = models.CharField(max_length=30, blank=True, verbose_name=_("Country"))
    pincode = models.CharField(max_length=8, blank=True, verbose_name=_("Pincode"))

    account_name = models.CharField(
        max_length=255, default="", blank=True, verbose_name=_("Account Name")
    )
    account_number = models.CharField(
        max_length=50, blank=True, verbose_name=_("Account Number")
    )
    bank_name = models.CharField(max_length=50, blank=True, verbose_name=_("Bank Name"))
    branch_name = models.CharField(
        max_length=50, blank=True, verbose_name=_("Branch Name")
    )
    branch_address = models.CharField(
        max_length=100, blank=True, verbose_name=_("Branch Address")
    )
    ifsc_code = models.CharField(max_length=30, blank=True, verbose_name=_("IFSC Code"))
    upi_qr_code = models.ImageField(
        upload_to="upi_qr_codes",
        default="sample.jpg",
        null=True,
        blank=True,
        verbose_name=_("UPI QR Code Image"),
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
        verbose_name = "Store"
        verbose_name_plural = "stores"
        ordering = ["-created_at"]
