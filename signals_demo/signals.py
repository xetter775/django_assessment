import time
import threading

from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Product
from .models import AuditLog


@receiver(post_save, sender=Product)
def signal_questions(sender, instance, **kwargs):

    print("\nSignal Started")

    print(
        "Signal Thread ID:",
        threading.current_thread().ident
    )

    time.sleep(5)

    AuditLog.objects.create(
        message=f"{instance.name} created"
    )

    print("Signal Finished\n")