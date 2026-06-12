import time

from django.core.management.base import BaseCommand

from signals_demo.models import Product


class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        start = time.time()

        Product.objects.create(
            name="Laptop"
        )

        end = time.time()

        print(
            f"Total Time: {end - start}"
        )