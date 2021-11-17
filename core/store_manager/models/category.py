import uuid

from config.models import ActivityTracking
from django.db import models
from django.utils.translation import gettext as _


# Create your models here.
class Category(ActivityTracking):

    name = models.CharField(
        max_length=50, blank=True, null=True, default="", verbose_name=_("Name")
    )
    image = models.ImageField(
        upload_to="category_image",
        default="sample.jpg",
        null=True,
        blank=True,
        verbose_name=_("Category Image"),
    )
    description = models.CharField(
        max_length=255, blank=True, verbose_name=_("Description")
    )

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
        verbose_name = "Category"
        verbose_name_plural = "categories"
        ordering = ["-created_at"]

    def get_absolute_url(self):
        return reverse("customadmin:category-list")


# Create your models here.
class SubCategory(ActivityTracking):

    parent_category = models.ForeignKey(
        "Category",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name=_("Parent Category"),
    )
    name = models.CharField(
        max_length=50, blank=True, null=True, default="", verbose_name=_("Name")
    )
    image = models.ImageField(
        upload_to="subcategory_image",
        default="sample.jpg",
        null=True,
        blank=True,
        verbose_name=_("Sub Category Image"),
    )
    description = models.CharField(
        max_length=255, blank=True, verbose_name=_("Description")
    )

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
        verbose_name = "Sub Category"
        verbose_name_plural = "sub categories"
        ordering = ["-created_at"]

    def get_absolute_url(self):
        return reverse("customadmin:subcategory-list")
