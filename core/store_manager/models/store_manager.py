import uuid

from config.models import ActivityTracking
from django.db import models
from django.utils.translation import gettext as _


# Create your models here.
class StoreManager(ActivityTracking):

    GENDER_CHOICES = (("Male", "MALE"), ("Female", "FEMALE"))

    store = models.ForeignKey(
        "Store", on_delete=models.CASCADE, blank=True, verbose_name=_("Store")
    )

    first_name = models.CharField(
        max_length=40, blank=True, verbose_name=_("Firstname")
    )
    last_name = models.CharField(max_length=40, blank=True, verbose_name=_("Lastname"))
    gender = models.CharField(
        choices=GENDER_CHOICES, max_length=40, blank=True, verbose_name=_("Gender")
    )
    birth_date = models.CharField(
        max_length=10, default="", blank=True, verbose_name=_("Birthdate")
    )
    email = models.EmailField(
        null=True, blank=True, unique=True, verbose_name=_("Email")
    )
    phone = models.CharField(
        max_length=20, default="", blank=True, verbose_name=_("Phone")
    )

    username = models.CharField(
        max_length=40,
        blank=True,
        null=True,
        default="",
        unique=True,
        verbose_name=_("Username"),
    )
    profile_image = models.ImageField(
        upload_to="delivery_boy_image",
        default="sample.jpg",
        null=True,
        blank=True,
        verbose_name=_("Delivery Boy Image"),
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

    otp = models.CharField(max_length=6, blank=True, default="", verbose_name=_("OTP"))

    unique_id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        verbose_name=_("Unique Id"),
    )

    is_active = models.BooleanField(default=True, verbose_name=_("Status"))

    def __unicode__(self):
        return self.email

    def get_full_name(self):
        return " ".join([self.first_name, self.last_name])

    def get_short_name(self):
        return self.first_name

    class Meta:
        verbose_name = "Store Manager"
        verbose_name_plural = "store managers"
        ordering = ["-created_at"]

    def get_absolute_url(self):
        return reverse("customadmin:storemanager-list")


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

    def get_absolute_url(self):
        return reverse("customadmin:storemanagerstatushistory-list")
