import re

from django.core.validators import validate_email
from django.core.exceptions import ValidationError

from videopath.apps.common import mailer

def send_share_mail(video, recipients, message):

	recipients = re.split("[\ ,]", recipients)

    # validate emails
	recipients_validated = []
	try:
	    for r in recipients:
	        if len(r.strip()) > 0:
	            validate_email(r)
	            recipients_validated.append(r)
	except ValidationError:
	    return False, "Could not parse recipients"

	if len(recipients_validated) == 0:
	    return False, "No valid recipients"

	mailer.send_share_mail(video, recipients, message)

	return True, ""