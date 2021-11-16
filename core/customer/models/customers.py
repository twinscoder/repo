import uuid
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext as _
from config.models import ActivityTracking

# Create your models here.
class Customer(ActivityTracking):

    GENDER_CHOICES = (("Male", "MALE"), ("Female", "FEMALE"))

    email = models.EmailField(null=True, blank=True, unique=True)
    username = models.CharField(
        max_length=40, blank=True, null=True, default="", unique=True
    )
    first_name = models.CharField(max_length=40, blank=True)
    last_name = models.CharField(max_length=40, blank=True)
    profile_image = models.ImageField(
        upload_to="profile_image",
        default="sample.jpg",
        null=True,
        blank=True,
        verbose_name=_("Profile Image"),
    )
    description = models.CharField(max_length=255, blank=True)
    birth_date = models.CharField(max_length=10, default="", blank=True)

    address = models.CharField(max_length=255, default="", blank=True)
    phone = models.CharField(max_length=20, default="", blank=True)
    city = models.CharField(max_length=50, blank=True)
    state = models.CharField(max_length=50, blank=True)
    country = models.CharField(max_length=30, blank=True)
    pincode = models.CharField(max_length=8, blank=True)
    otp = models.CharField(max_length=6, blank=True, default=000000)

    unique_id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        verbose_name=_("Unique Id"),
    )

    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.email

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
