import uuid

from config.models import ActivityTracking
from django.db import models
from django.utils.translation import gettext as _


# Create your models here.
class Product(ActivityTracking):

    name = models.CharField(
        max_length=50, blank=True, null=True, default="", verbose_name=_("Name")
    )
    alias = models.CharField(
        max_length=50, blank=True, null=True, default="", verbose_name=_("Alias")
    )
    category = models.ForeignKey(
        "Category",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        default="",
        verbose_name=_("Category"),
    )
    subcategory = models.ForeignKey(
        "SubCategory",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        default="",
        verbose_name=_("Subcategory"),
    )
    store = models.ForeignKey(
        "Store",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        default="",
        verbose_name=_("Store"),
    )
    coupon = models.ManyToManyField("Coupon", blank=True, verbose_name=_("Coupons"))
    image = models.ImageField(
        upload_to="product_image",
        default="sample.jpg",
        null=True,
        blank=True,
        verbose_name=_("Product Image"),
    )
    description = models.CharField(
        max_length=255, blank=True, verbose_name=_("Description")
    )

    purchase_price = models.FloatField(
        default=0, blank=True, null=True, verbose_name=_("Purchase Price")
    )
    selling_price = models.FloatField(
        default=0, blank=True, null=True, verbose_name=_("Selling Price")
    )
    membership_price = models.FloatField(
        default=0, blank=True, null=True, verbose_name=_("Membership Price")
    )

    stock = models.BooleanField(default=True, verbose_name=_("Stock"))
    unit = models.IntegerField(default=0, verbose_name=_("Unit"))

    cancel_available = models.BooleanField(
        default=True, verbose_name=_("Cancel Available")
    )
    free_shipping = models.BooleanField(default=True, verbose_name=_("Free Shipping"))
    cash_on_delivery = models.BooleanField(
        default=True, verbose_name=_("Cash on Delivery")
    )

    unique_id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        verbose_name=_("Unique Id"),
    )
    is_deleted = models.BooleanField(default=False, verbose_name=_("Is Deleted"))
    is_active = models.BooleanField(default=True, verbose_name=_("Status"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "products"
        ordering = ["-created_at"]
