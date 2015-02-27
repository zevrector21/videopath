from django.conf import settings
from mandrill import Mandrill

logger = settings.LOGGER

#
# for now, just abstract the mandrill sending here
#
def mandrill_send(message):

    # prefix messages sent from dev
    subject_prefix = "[Dev] " if (settings.STAGING or settings.LOCAL or settings.CONTINOUS_INTEGRATION) else ""
    message["subject"] = subject_prefix + message.get("subject", 0)

    try:
        m = Mandrill(settings.MANDRILL_APIKEY)
        m.messages.send(message=message, async=False, ip_pool='Main Pool')
    except:
        logger.error("error sending mail")