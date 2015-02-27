from django.core.management.base import BaseCommand

from videopath.apps.users.util import auto_mail_util


class Command(BaseCommand):

    def handle(self, *args, **options):
        auto_mail_util.send_welcome_mails()
        auto_mail_util.send_retention_mails()
