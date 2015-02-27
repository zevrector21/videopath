from django.core.management.base import BaseCommand

from videopath.apps.payments.util import payment_util

class Command(BaseCommand):

    def handle(self, *args, **options):
        payment_util.process_payments()
