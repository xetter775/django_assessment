from django.core.management.base import BaseCommand
from django.db import transaction

from signals_demo.models import Product
from signals_demo.models import AuditLog


class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        Product.objects.all().delete()
        AuditLog.objects.all().delete()

        try:

            with transaction.atomic():

                Product.objects.create(
                    name="Tablet"
                )

                raise Exception(
                    "Rollback Transaction"
                )

        except Exception as e:

            print(e)

        print(
            "Products Count:",
            Product.objects.count()
        )

        print(
            "Audit Logs Count:",
            AuditLog.objects.count()
        )