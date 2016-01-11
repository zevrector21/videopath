import datetime

#
# register all mail types
#
mails = {

	#
	# signup sent after user signs up for our app
	#
	'signup': {
		'subject': "Hello from Videopath!"
	},


	'forgot_password': {
		'subject': "Videopath Password Reset"
	},

	#
	# subscriptions etc
	#
	'subscribe_will_change': {
		'subject': 'Subscription Info'
	},

	'subscribe_change': {
		'subject': 'Subscription Info'
	},

	'invoice_created': {
		'subject': "Videopath billing"
	},


	#
	# quota
	#
	'quota_warning': {
		'subject': "You have almost used up your quota this month"
	},

	'quota_exceeded': {
		'subject': "You have exceeded your quota this month"
	},

	#
	# transcoding
	#
	'jpg_transcode_failed': {
		'subject': 'iPhone Trancoding Failed'
	},


	'jpg_transcode_succeeded': {
		'subject': 'iPhone Trancoding Succeeded'
	},

	'transcode_complete': {
		'subject': 'Your video is ready to edit'
	},

	'transcode_error': {
		'subject': 'Error processing your video'
	},


	#
	# Follow up emails
	#
	'welcome': {
		'subject': "How's Videopath working?",
		'agent': 'support'
	},

	'follow_up_three_weeks': {
		'subject': "Get the most out of Videopath",
		'agent': 'support'
	},

	'follow_up_six_weeks': {
		'subject': "Make Videopath work for you!",
		'agent': 'support'
	}

}

#
# agents
#
agents = {

	"default": {
    	"email": "support@videopath.com",
        "name": "Videopath Team"
    },

    "support": {
        "email": "desiree@videopath.com",
        "name": "Desiree dela Rosa"
    },

}

#
# data for displaying the test versions of the mail
#
test_data = {

	'forgot_password': {
		'password': '980LJSJ3n'
	},


	#
	# subscriptions etc
	#
	'subscribe_will_change': {
		'plan': 'Pro',
		'switch_date': datetime.date.today()
	},

	'subscribe_change': {
		'interval': 'Month',
		'plan': 'Pro',
		'is_free': False
	},

	'invoice_created': {
		'subject': "Videopath billing"
	},


	#
	# transcoding
	#
	'jpg_transcode_failed': {
		'title': "My Project"
	},

	'jpg_transcode_succeeded': {
		'title': "My Project"
	},


	'transcode_complete': {
		'title': "My Project",
		'video_id': "12345678"
	},

	'transcode_error': {
		'title': "My Project"
	},

	'invoice_created': {
		"amount_due": 640000,
        "link": 'some_url',
        "currency": "EUR"
	}


}