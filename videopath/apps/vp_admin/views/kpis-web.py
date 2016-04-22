from datetime import timedelta, date
import itertools

from django.http import HttpResponseRedirect
from django.template.response import SimpleTemplateResponse
from django.contrib.auth.models import User
from django.core.cache import cache
from .decorators import group_membership_required

from videopath.apps.vp_admin.views import helpers
from videopath.apps.videos.models import Video


from videopath.apps.analytics.services.ga_import_service import _get_service

def website_traffic():
	service = _get_service()
	args = {
        'ids': 'ga:80030959',
        'metrics': 'ga:sessions',
        'start_date': '60daysAgo',
        'end_date': 'today',
        'dimensions': 'ga:week,ga:year'
    }

	result = service.data().ga().get(**args).execute()
	result = map(lambda x: [str(x[0]) + ' ' + str(x[1]), int(x[2])], result['rows'])
	return helpers.chart([['Week', 'Visitors']] + result, 'line')

# build the view
@group_membership_required('insights')
def view(request):

	result = ""

	result += helpers.header("Website traffic")
	result += website_traffic()

	result += helpers.header("Website traffic sources")

	result += helpers.header("Blog traffic")
	result += helpers.header("Blog traffic sources")

	result += helpers.header("Player sessions")
	result += helpers.header("Player plays")


	return SimpleTemplateResponse("insights/base.html", {
	    "title": "KPIs Web",
	    "insight_content": result
	    })


