# import uuid

# from config.models import ActivityTracking
# from django.db import models
# from django.utils.translation import gettext as _

# # Create your models here.
# class Order(ActivityTracking):

#     ORDER_STATUS_CHOICES = (
#         ("Pending")("Pending"),
#         ("Inprocess")("Inprocess"),
#         ("Dispatched")("Dispatched"),
#         ("Delivered")("Delivered"),
#         ("Return")("Return"),
#         ("Cancel")("Cancel"),
#     )

#     order_status = models.CharField(
#         choices=ORDER_STATUS_CHOICES,
#         blank=True,
#         null=True,
#         verbose_name=_("Order Status"),
#     )
#     customer = models.ForeignKey(
#         Customer,
#         on_delete=models.CASCADE,
#         blank=True,
#         null=True,
#         verbose_name=_("Store"),
#     )
#     store = models.ManyToManyField(
#         "Store",
#         on_delete=models.SET_NULL,
#         blank=True,
#         verbose_name=_("Stores"),
#     )
#     product = models.ManyToManyField(
#         Product,
#         on_delete=models.SET_NULL,
#         blank=True,
#         verbose_name=_("Products"),
#     )
#     total_qty = models.IntegerField(
#         default=0, blank=True, null=True, verbose_name=_("Amount")
#     )
#     total_amount = models.FloatField(
#         default=0, blank=True, null=True, verbose_name=_("Amount")
#     )
#     order_datetime = models.DateTimeField(blank=True)
#     status = models.BooleanField(default=False)
#     payment_method = models.BooleanField(default=False)

#     unique_id = models.UUIDField(
#         default=uuid.uuid4,
#         editable=False,
#         unique=True,
#         verbose_name=_("Unique Id"),
#     )
#     is_active = models.BooleanField(default=True, verbose_name=_("Status"))

#     def __unicode__(self):
#         return self.name

#     class Meta:
#         verbose_name = "Expense"
#         verbose_name_plural = "expense"
#         ordering = ["-created_at"]

#     def get_absolute_url(self):
#         return reverse("customadmin:expense-list")
