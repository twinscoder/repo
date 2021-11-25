import uuid

from config.models import ActivityTracking
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models
from django.utils.translation import gettext as _
from django.urls import reverse

# Create your models here.


class AccountManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError("Users must have a valid email address.")

        if not kwargs.get("username"):
            raise ValueError("Users must have a valid username.")

        account = self.model(
            email=self.normalize_email(email), username=kwargs.get("username")
        )

        account.set_password(password)
        account.save()

        return account

    def create_superuser(self, email, password, **kwargs):
        account = self.create_user(email, password, **kwargs)

        account.is_superuser = True
        account.is_staff = True
        account.save()

        return account


class User(AbstractBaseUser, ActivityTracking, PermissionsMixin):

    ADMIN = "Admin"
    MANAGER = "Manager"

    ROLE_CHOICES = (
        (ADMIN, "Admin"),
        (MANAGER, "Manager"),
    )

    email = models.EmailField(
        null=True, blank=True, unique=True, verbose_name=_("Email")
    )
    username = models.CharField(
        max_length=40,
        blank=True,
        null=True,
        default="",
        unique=True,
        verbose_name=_("Username"),
    )
    first_name = models.CharField(
        max_length=40, blank=True, verbose_name=_("Firstname")
    )
    last_name = models.CharField(max_length=40, blank=True, verbose_name=_("Lastname"))
    role = models.CharField(
        choices=ROLE_CHOICES, max_length=40, blank=True, verbose_name=_("Role")
    )
    profile_image = models.ImageField(
        upload_to="profile_image",
        default="sample.jpg",
        null=True,
        blank=True,
        verbose_name=_("Profile Image"),
    )
    description = models.CharField(
        max_length=255, blank=True, verbose_name=_("Description")
    )

    birth_date = models.CharField(
        max_length=10, default="", blank=True, verbose_name=_("Birthdate")
    )
    address = models.CharField(
        max_length=255, default="", blank=True, verbose_name=_("Address")
    )
    phone = models.CharField(
        max_length=20, default="", blank=True, verbose_name=_("Phone")
    )
    city = models.CharField(max_length=50, blank=True, verbose_name=_("City"))
    state = models.CharField(max_length=50, blank=True, verbose_name=_("State"))
    country = models.CharField(max_length=30, blank=True, verbose_name=_("Country"))
    pincode = models.CharField(max_length=8, blank=True, verbose_name=_("Pincode"))

    unique_id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        verbose_name=_("Unique Id"),
    )

    is_manager = models.BooleanField(default=False, verbose_name=_("Is Manager"))
    is_active = models.BooleanField(default=True, verbose_name=_("Is Active"))
    is_staff = models.BooleanField(default=True, verbose_name=_("Is Staff"))

    objects = AccountManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.username

    def get_full_name(self):
        return " ".join([self.first_name, self.last_name])

    def get_short_name(self):
        return self.first_name

    def get_absolute_url(self):
        return reverse("customadmin:index")

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ["-created_at"]
