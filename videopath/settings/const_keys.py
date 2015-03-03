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
GA_USERNAME = "videopath.dev"
GA_PASSWORD = os.environ.get("GA_PASSWORD")

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