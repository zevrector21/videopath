import conf

from django.template import Context
from django.template.loader import get_template

from django.template.response import HttpResponse, SimpleTemplateResponse
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def view(request):
	return SimpleTemplateResponse("insights/base.html", {
	    })

@staff_member_required
def mailview(request, mail, mailtype):

	# mailconf = conf.mails.get(mail)
	testconf = conf.test_data.get(mail)
	testconf.update({'username': request.user.username})

	print conf.test_data
	print testconf

	c = Context(testconf)
	t = get_template('mails/' + mail + '.' + mailtype)
	message = t.render(c)



	if mailtype == 'txt':
		c = Context({'mail': message})
		t = get_template('qa/plain_mail_wrapper.html')
		message = t.render(c)

	return HttpResponse(message)
