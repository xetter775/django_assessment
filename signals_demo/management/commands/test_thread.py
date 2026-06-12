import threading

from django.core.management.base import BaseCommand

from signals_demo.models import Product


class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        print(
            "Caller Thread ID:",
            threading.current_thread().ident
        )

        Product.objects.create(
            name="Phone"
        )