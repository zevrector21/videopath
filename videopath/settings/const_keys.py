import os

#
# mandrill
#
MANDRILL_APIKEY = os.environ.get("MANDRILL_APIKEY")

#
# mail chimp
#
MAILCHIMP_APIKEY = os.environ.get("MAILCHIMP_APIKEY")

#
# Stripe
#
STRIPE_API_KEY = os.environ.get("STRIPE_API_KEY")

#
# GA access
#
GA_EMAIL = os.environ.get("GA_EMAIL")
GA_PRIVATE_KEY = os.environ.get("GA_PRIVATE_KEY")

#
# AWS
#
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")

#
# Raven config
#
RAVEN_CONFIG = {
    'dsn': os.environ.get("RAVEN_KEY"),
}

#
# Slack
#
SLACK_API_TOCKEN = os.environ.get("SLACK_API_TOCKEN")

#
#	Mailchimp Oauth
#
MAILCHIMP_CLIENT_ID = os.environ.get("MAILCHIMP_CLIENT_ID")
MAILCHIMP_CLIENT_SECRET = os.environ.get("MAILCHIMP_CLIENT_SECRET")