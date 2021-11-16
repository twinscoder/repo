import uuid
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext as _
from config.models import ActivityTracking

# Create your models here.
class Category(ActivityTracking):

    parent_category = models.ForeignKey(
        "Category", on_delete=models.CASCADE, blank=True, null=True
    )
    name = models.CharField(max_length=50, blank=True, null=True, default="")
    image = models.ImageField(
        upload_to="category_image",
        default="sample.jpg",
        null=True,
        blank=True,
        verbose_name=_("Category Image"),
    )
    description = models.CharField(max_length=255, blank=True)

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
        verbose_name = "Category"
        verbose_name_plural = "categories"
        ordering = ["-created_at"]

    def get_absolute_url(self):
        return reverse("customadmin:category-list")
