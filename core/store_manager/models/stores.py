import uuid
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext as _
from config.models import ActivityTracking

# Create your models here.
class Store(ActivityTracking):

    name = models.CharField(max_length=40, blank=True, null=True, default="")
    business_email = models.EmailField(
        max_length=100, blank=True, null=True, default="", unique=True
    )
    phone = models.CharField(max_length=20, blank=True)
    image = models.ImageField(
        upload_to="store_image",
        default="sample.jpg",
        null=True,
        blank=True,
        verbose_name=_("Store Image"),
    )
    description = models.CharField(max_length=255, blank=True)

    address = models.CharField(max_length=255, default="", blank=True)
    city = models.CharField(max_length=50, blank=True)
    state = models.CharField(max_length=50, blank=True)
    country = models.CharField(max_length=30, blank=True)
    pincode = models.CharField(max_length=8, blank=True)

    account_name = models.CharField(max_length=255, default="", blank=True)
    account_number = models.CharField(max_length=50, blank=True)
    bank_name = models.CharField(max_length=50, blank=True)
    branch_name = models.CharField(max_length=50, blank=True)
    branch_address = models.CharField(max_length=100, blank=True)
    ifsc_code = models.CharField(max_length=30, blank=True)
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
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "Store"
        verbose_name_plural = "stores"
        ordering = ["-created_at"]

    def get_absolute_url(self):
        return reverse("customadmin:store-list")
