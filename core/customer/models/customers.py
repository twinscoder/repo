import uuid

from config.models import ActivityTracking
from django.db import models
from django.utils.translation import gettext as _


# Create your models here.
class Customer(ActivityTracking):

    GENDER_CHOICES = (("Male", "Male"), ("Female", "Female"))

    first_name = models.CharField(
        verbose_name=_("Firstname"), max_length=40, blank=True
    )
    last_name = models.CharField(verbose_name=_("Lastname"), max_length=40, blank=True)
    gender = models.CharField(
        verbose_name=_("Gender"), choices=GENDER_CHOICES, max_length=40, blank=True
    )
    birth_date = models.CharField(
        verbose_name=_("Birthdate"), max_length=10, default="", blank=True
    )
    email = models.EmailField(
        verbose_name=_("Email"), null=True, blank=True, unique=True
    )
    phone = models.CharField(
        verbose_name=_("Phone"), max_length=20, default="", blank=True
    )

    username = models.CharField(
        verbose_name=_("Username"),
        max_length=40,
        blank=True,
        null=True,
        default="",
        unique=True,
    )
    profile_image = models.ImageField(
        upload_to="profile_image",
        default="sample.jpg",
        null=True,
        blank=True,
        verbose_name=_("Profile Image"),
    )
    description = models.CharField(
        verbose_name=_("Description"), max_length=255, blank=True
    )

    address = models.CharField(
        verbose_name=_("Address"), max_length=255, default="", blank=True
    )
    city = models.CharField(verbose_name=_("City"), max_length=50, blank=True)
    state = models.CharField(verbose_name=_("State"), max_length=50, blank=True)
    country = models.CharField(verbose_name=_("Country"), max_length=30, blank=True)
    pincode = models.CharField(verbose_name=_("Pincode"), max_length=8, blank=True)

    otp = models.CharField(verbose_name=_("OTP"), max_length=6, blank=True, default="")
    fcm_token = models.CharField(
        verbose_name=_("FCM Token"), max_length=6, blank=True, default=""
    )
    refer_code = models.CharField(
        verbose_name=_("Refer Code"), max_length=8, blank=True, default=""
    )
    refer_from = models.ForeignKey(
        "Customer",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name=_("Refer From"),
    )

    unique_id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        verbose_name=_("Unique Id"),
    )

    is_active = models.BooleanField(default=True, verbose_name=_("Status"))

    def __str__(self):
        return self.username

    def get_full_name(self):
        return " ".join([self.first_name, self.last_name])

    def get_short_name(self):
        return self.first_name

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "customers"
        ordering = ["-created_at"]

    def get_absolute_url(self):
        return reverse("customadmin:customer-list")


class CustomerStatusHistory(ActivityTracking):

    customer = models.ForeignKey(
        "Customer", on_delete=models.CASCADE, blank=True, verbose_name=_("Customer")
    )
    status = models.BooleanField(default=False, verbose_name=_("Status"))
    reason = models.CharField(max_length=255, blank=True, verbose_name=_("Reason"))

    def __str__(self):
        return self.customer.username

    class Meta:
        verbose_name = "Customer Status History"
        verbose_name_plural = "customers status history"
        ordering = ["-created_at"]

    def get_absolute_url(self):
        return reverse("customadmin:customerstatushistory-list")
