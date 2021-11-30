from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import StoreProduct


@receiver(post_delete, sender=StoreProduct)
def delete_store_product(sender, instance, **kwargs):
    a = StoreProduct.objects.filter(priority_index__gt=instance.priority_index)
    print("➡ a :", a)
    print("➡ a ________________________________:")
