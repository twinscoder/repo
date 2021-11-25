import uuid

from config.models import ActivityTracking
from django.db import models
from django.utils.translation import gettext as _


# Create your models here.
class Coupon(ActivityTracking):
    FIXED = "Fixed"
    PERCENTAGE = "Percentage"
    SPECIAL = "Special"

    DISCOUNT_CHOICES = (
        (FIXED, "Fixed"),
        (PERCENTAGE, "Percentage"),
        (SPECIAL, "Special"),
    )

    code = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        default="",
        unique=True,
        verbose_name=_("Cuopon Code"),
    )
    discount_percentage = models.FloatField(
        max_length=3,
        blank=True,
        null=True,
        default=0,
        verbose_name=_("Discount in Percentage (%)"),
    )
    category = models.ManyToManyField(
        "Category",
        blank=True,
        verbose_name=_("Category"),
        help_text="If you select category then it apply to related all",
    )
    sub_category = models.ManyToManyField(
        "SubCategory",
        blank=True,
        verbose_name=_("SubCategory"),
        help_text="If you select subcategory then it apply to related all",
    )
    product = models.ManyToManyField(
        "Product",
        blank=True,
        verbose_name=_("Product"),
        help_text="If you select product then it apply to related product",
    )
    discount_amount = models.FloatField(
        max_length=5,
        blank=True,
        null=True,
        default=0,
        verbose_name=_("Discount Amount"),
    )
    discount_type = models.CharField(
        choices=DISCOUNT_CHOICES,
        max_length=20,
        blank=True,
        verbose_name=_("Discount Type"),
    )
    is_repeatable = models.BooleanField(default=True, verbose_name=_("Is Repeatable"))
    min_amount = models.FloatField(
        blank=True, null=True, default=0, verbose_name=_("Min Purchase Amount")
    )
    buy_product_count = models.IntegerField(
        blank=True, null=True, default=1, verbose_name=_("Buy Number of Product")
    )
    get_free_product_count = models.IntegerField(
        blank=True, null=True, default=1, verbose_name=_("Get Number of Product Free")
    )
    description = models.CharField(
        max_length=255, blank=True, verbose_name=_("Description")
    )
    count = models.IntegerField(default=0, verbose_name=_("Count"))

    unique_id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        verbose_name=_("Unique Id"),
    )
    is_billable = models.BooleanField(default=True, verbose_name=_("is Billable"))
    is_active = models.BooleanField(default=True, verbose_name=_("Status"))

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = "Coupon"
        verbose_name_plural = "coupons"
        ordering = ["-created_at"]
