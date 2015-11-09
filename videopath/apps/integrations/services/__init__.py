
from . import mailchimp_service
from . import brightcove_service

config = {

	'mailchimp': {
		'id': 'mailchimp',
		'title': 'Mailchimp',
		'description': 'Use Mailchimp to capture your viewers email addresses.',
		'credentials': False,
		'module': mailchimp_service
	},

	'brightcove': {
		'id': 'brightcove',
		'title': 'Brightcove',
		'description': 'Use Brightcove to host your videos',
		'credentials': [{
				'name': 'Brightcove Client ID',
				'id': 'client_id'
			}, {
				'name': 'Brightcove Client Secret',
				'id': 'client_secret'
			}
		],
		'module': brightcove_service
	}
	
}