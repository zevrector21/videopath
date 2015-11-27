from inlinestyler.utils import inline_css

from django.template import Context

import sendgrid
from django.template.loader import get_template


# dev


def run():

	#
	# check api key
	#
	sg = sendgrid.SendGridAPIClient(API_KEY)
	status, msg = sg.apikeys.get()
	print status
	t = get_template("mails/share_video.html")
	message_html = t.render(Context({}))
	message_html = inline_css(message_html)


	#
	# send mail
	#
	sg = sendgrid.SendGridClient(API_KEY)
	message = sendgrid.Mail()

	message.add_to("dscharf@gmx.net")
	message.set_from("app@videopath.com")
	message.set_subject("Sending with SendGrid is Fun")
	message.set_html(message_html)

	message.add_category('testing')


	sg.send(message)
	print 'sent'