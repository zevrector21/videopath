from datetime import timedelta, datetime

from django.contrib.auth.models import User

from videopath.apps.common import mailer
from videopath.apps.users.models import AutomatedMail


# send welcome mails
def send_welcome_mails():
    thresh = datetime.now() - timedelta(days=7)
    users = User.objects.filter(
        date_joined__lte=thresh).prefetch_related('automated_mails')
    count = 0
    for u in users:
        if u.automated_mails.filter(mailtype=AutomatedMail.TYPE_WELCOME).count() == 0:
            send_welcome_mail(u)
            count += 1
        if count >= 10:
            break

def send_welcome_mail(user):
    mailer.send_welcome_mail(user)
    AutomatedMail.objects.create(
        mailtype=AutomatedMail.TYPE_WELCOME, user=user)


def send_retention_mails():
    pass
