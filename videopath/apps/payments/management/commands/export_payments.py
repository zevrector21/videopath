from django.core.management.base import BaseCommand

from videopath.apps.payments.util import payment_export_util
from videopath.apps.payments.models import Payment

class Command(BaseCommand):

    def handle(self, *args, **options):
    	for p in Payment.objects.filter(paid=True):
        	payment_export_util.export_payment(p)
