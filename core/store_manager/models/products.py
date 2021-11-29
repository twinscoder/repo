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
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        default="",
        verbose_name=_("Category"),
    )
    subcategory = models.ForeignKey(
        "SubCategory",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        default="",
        verbose_name=_("Subcategory"),
    )
    image = models.ImageField(
        upload_to="product_image",
        default="sample.jpg",
        null=True,
        blank=True,
        verbose_name=_("Product Image"),
    )
    small_description = models.CharField(
        max_length=255, blank=True, verbose_name=_("Small Description")
    )
    long_description = models.CharField(
        max_length=300, blank=True, verbose_name=_("Long Description")
    )

    unique_id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        verbose_name=_("Unique Id"),
    )
    is_active = models.BooleanField(default=True, verbose_name=_("Status"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "products"
        ordering = ["-created_at"]


class StoreProduct(ActivityTracking):

    store = models.ForeignKey(
        "Store",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name=_("Store"),
    )
    product = models.ForeignKey(
        "Product",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name=_("Product"),
    )
    priority_index = models.IntegerField(
        default=0, blank=True, null=True, verbose_name=_("Priority Index")
    )
    stock = models.BooleanField(default=True, verbose_name=_("Stock"))
    unit = models.IntegerField(default=0, verbose_name=_("Unit"))

    purchase_price = models.FloatField(
        default=0, blank=True, null=True, verbose_name=_("Purchase Price")
    )
    selling_price = models.FloatField(
        default=0, blank=True, null=True, verbose_name=_("Selling Price")
    )
    membership_price = models.FloatField(
        default=0, blank=True, null=True, verbose_name=_("Membership Price")
    )
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
    is_active = models.BooleanField(default=True, verbose_name=_("Status"))

    def __str__(self):
        return f"{self.store.name} - {self.product.name}"

    class Meta:
        verbose_name = "Store Product"
        verbose_name_plural = "store products"
        ordering = ["-created_at"]
