import conf

from django.template import Context
from django.template.loader import get_template

from django.template.response import HttpResponse, SimpleTemplateResponse
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def view(request):

	mail = request.GET.get('mail', 'signup')
	mailtype = request.GET.get('mailtype', 'html')

	mailconf = conf.mails.get(mail)


	return SimpleTemplateResponse("qa/mails.html", {
			'mails': conf.mails.keys(),
			'mailsubject': mailconf['subject'],
			'mail': mail,
			'mailtype': mailtype
	    })

@staff_member_required
def mailview(request, mail, mailtype):

	testconf = conf.test_data.get(mail, {})
	testconf.update({'username': request.user.username})

	c = Context(testconf)
	t = get_template('mails/{0}.{1}'.format(mail, mailtype))
	message = t.render(c)

	if mailtype == 'txt':
		c = Context({'mail': message})
		t = get_template('qa/plain_mail_wrapper.html')
		message = t.render(c)

	return HttpResponse(message)
