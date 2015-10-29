from .decorators import group_membership_required
from django.http import HttpResponse
import csv
import datetime

from django.contrib.auth.models import User


def build_csv_response(data):
	response = HttpResponse(content_type='text/csv') 
	writer = csv.writer(response)

	for row in data:
		writer.writerow(row)

	return response

@group_membership_required('exports')
def newest_users(request):

	rows = []
	rows.append(['List exported on ' + str(datetime.date.today())])
	rows.append(['----------------'])

	rows.append(
		['ID', 'Username', 'Email', 'Date Joined','-',
		 'Country', 'Referrer', 'Campaign', '-',
		 'Videos created', 'Videos Published'
		])

	days = int(request.GET.get('days', 7))
	date = datetime.date.today() - datetime.timedelta(days=days)


	# build row from user
	for user in User.objects.filter(date_joined__gte=date).order_by('-date_joined'):

		# standard data
		row = [user.pk, user.username, user.email, user.date_joined.date()]
		row.append('-')

		# signup data
		try:
			row.extend([user.campaign_data.country, user.campaign_data.referrer, user.campaign_data.name])
		except:
			row.extend(['', '', ''])
		row.append('-')

		row.extend([user.videos.count(), user.videos.filter(published=True).count()]  )


		rows.append(row)


	return build_csv_response(rows)
