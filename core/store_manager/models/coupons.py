import uuid
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext as _
from config.models import ActivityTracking

# Create your models here.
class Coupon(ActivityTracking):

    code = models.CharField(max_length=50, blank=True, null=True, default="")
    amount = models.FloatField(max_length=3, blank=True, null=True, default=0)
    min_amount = models.FloatField(max_length=10, blank=True, null=True, default=0)
    expiry_date = models.DateTimeField(blank=True, null=True, default="")
    description = models.CharField(max_length=255, blank=True)
    only_for_members = models.BooleanField(default=False)
    count = models.IntegerField(default=0)

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
        verbose_name = "Coupon"
        verbose_name_plural = "coupons"
        ordering = ["-created_at"]

    def get_absolute_url(self):
        return reverse("customadmin:coupon-list")
