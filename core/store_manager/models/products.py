import uuid
from django.db import models
from django.db.models.deletion import SET_NULL
from django.utils.translation import gettext as _
from config.models import ActivityTracking

# Create your models here.
class Product(ActivityTracking):

    name = models.CharField(max_length=50, blank=True, null=True, default="")
    alias = models.CharField(max_length=50, blank=True, null=True, default="")
    category = models.ForeignKey(
        "Category", on_delete=models.CASCADE, blank=True, null=True, default=""
    )
    store = models.ForeignKey(
        "Store", on_delete=models.SET_NULL, blank=True, null=True, default=""
    )
    coupon = models.ManyToManyField("Coupon", blank=True)
    image = models.ImageField(
        upload_to="product_image",
        default="sample.jpg",
        null=True,
        blank=True,
        verbose_name=_("Product Image"),
    )
    description = models.CharField(max_length=255, blank=True)

    purchase_price = models.FloatField(default=0, blank=True, null=True)
    selling_price = models.FloatField(default=0, blank=True, null=True)
    membership_price = models.FloatField(default=0, blank=True, null=True)

    stock = models.BooleanField(default=True)
    unit = models.IntegerField(default=0)

    cancle_available = models.BooleanField(default=True)
    free_shipping = models.BooleanField(default=True)
    cash_on_delivery = models.BooleanField(default=True)

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
        verbose_name = "Product"
        verbose_name_plural = "products"
        ordering = ["-created_at"]

    def get_absolute_url(self):
        return reverse("customadmin:product-list")
