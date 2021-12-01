import uuid

from config.models import ActivityTracking
from django.db import models
from django.utils.translation import gettext as _
from core.customer.models import Customer, CustomerAddress

# Create your models here.
class Order(ActivityTracking):

    PENDING = "Pending"
    IN_PROGRESS = "In Progress"
    DISPATCHED = "Dispatched"
    DELIVERED = "Delivered"
    RETURN = "Return"
    CANCEL = "Cancel"
    ORDER_STATUS_CHOICES = (
        (PENDING, "Pending"),
        (IN_PROGRESS, "Inprocess"),
        (DISPATCHED, "Dispatched"),
        (DELIVERED, "Delivered"),
        (RETURN, "Return"),
        (CANCEL, "Cancel"),
    )

    COD = "COD"
    ONLINE = "Online"
    PAYMENT_METHOD_CHOICES = (
        (COD, "COD"),
        (ONLINE, "Online"),
    )

    order_status = models.CharField(
        max_length=50,
        choices=ORDER_STATUS_CHOICES,
        blank=True,
        null=True,
        verbose_name=_("Order Status"),
    )
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name=_("Customer"),
    )
    store = models.ForeignKey(
        "Store",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name=_("Store"),
    )
    product = models.ManyToManyField(
        "Product",
        blank=True,
        verbose_name=_("Products"),
    )
    total_qty = models.IntegerField(
        default=0, blank=True, null=True, verbose_name=_("Total Quantity")
    )
    total_amount = models.FloatField(
        default=0, blank=True, null=True, verbose_name=_("Total Amount")
    )
    order_datetime = models.DateTimeField(blank=True, verbose_name=_("Order Datetime"))
    status = models.BooleanField(default=False, verbose_name=_("Accepted / Declined"))
    reason = models.CharField(
        default="", max_length=50, blank=True, null=True, verbose_name=_("Reason")
    )
    payment_method = models.CharField(
        max_length=50,
        choices=PAYMENT_METHOD_CHOICES,
        default=False,
        verbose_name=_("Payment Method"),
    )
    discount_amount = models.FloatField(
        default=0, blank=True, null=True, verbose_name=_("Discount Amount")
    )
    shipping_charge = models.FloatField(
        default=0, blank=True, null=True, verbose_name=_("Shipping Charge")
    )
    # billing_address = models.ForeignKey(
    #     CustomerAddress,
    #     on_delete=models.SET_NULL,
    #     blank=True,
    #     verbose_name=_("Billing Address"),
    # )
    shipping_address = models.ForeignKey(
        CustomerAddress,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name=_("Shipping Address"),
    )
    coupon = models.ForeignKey(
        "Coupon",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name=_("Coupon"),
    )
    discount_type = models.CharField(
        default="",
        max_length=50,
        blank=True,
        null=True,
        verbose_name=_("Discount Type"),
    )
    order_number = models.CharField(
        default="",
        max_length=50,
        blank=True,
        null=True,
        verbose_name=_("Order Number"),
    )
    billing_number = models.CharField(
        default="",
        max_length=50,
        blank=True,
        null=True,
        verbose_name=_("Billing Number"),
    )

    unique_id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        verbose_name=_("Unique Id"),
    )

    def __unicode__(self):
        return self.order_number

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "orders"
        ordering = ["-created_at"]

    def get_absolute_url(self):
        return reverse("customadmin:order-list")
