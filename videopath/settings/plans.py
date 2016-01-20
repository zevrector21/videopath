
#
# List of available features
#
PLAN_FEATURES = [
	'feature_upload',
	'feature_vimeo',
	'feature_brightcove',
	'feature_own_hosting',
    'feature_wistia',
    'feature_custom_hosting',
   	'feature_endscreen',
	'feature_advanced_settings',
	'feature_advanced_library',
	'feature_email_collector',
    'feature_integrations',
    'feature_custom_analytics',
    'feature_teams', 
    'feature_theme',
    'feature_icon',
    'feature_advanced_video_settings', 
    'feature_dev'
]

PLAN_DEFAULTS = {

	'subscribable': False,
	'listable': False,

	'group-alias': [],
	'group': 'free',

    'max_projects': 5000,
    'max_views_month': 10000000,
    'name': 'Videopath Plan',
    'price_eur': 0,
    'price_usd': 0,
    'price_gbp': 0,
    'payment_interval': 'month',
    'value': 1
}

PLANS = {

	###################
	# CURRENT
	###################

	# free plan, simple
    'free': {

        'group': 'free',
        'subscribable': True,
        
        #
        # variants
        #
        'variants': {
            'free': {
                'name': 'Free',
                'price_eur': 0,
                'price_usd': 0,
                'price_gbp': 0,
                'payment_interval': 'month',
                'value': 1000,
            }
        }

    },


    # starter plan with 2 variants
    '201509-starter': {

        'group': 'starter',
        'subscribable': True,
        

        #
        # features
        #
        'feature_endscreen': True,
        'feature_advanced_library': True,

        #
        # variants
        #
        'variants': {

            'yearly': {
                'name': 'Basic Yearly',
                'price_eur': 80000,
                'price_usd': 100000,
                'price_gbp': 65000,
                'payment_interval': 'year',
                'value': 2003,
            },

            'monthly': {
                'name': 'Basic Monthly',
                'price_eur': 7900,
                'price_usd': 9900,
                'price_gbp': 5900,
                'payment_interval': 'month',
                'value': 2002,
            },

            'monthly-15': {
                'name': 'Basic Monthly',
                'price_eur': 1500,
                'price_usd': 2000,
                'price_gbp': 1200,
                'payment_interval': 'month',
                'value': 2001,
                'subscribable': False
            }

        }

    },

    # pro plan
    '201412-pro-plus': {

        'group': 'pro-plus',
        'subscribable': True,

        #
        # features
        #
        'feature_endscreen': True,
        'feature_advanced_settings': True,
        'feature_vimeo': True,
        'feature_wistia': True,
        'feature_custom_analytics': True,
        'feature_custom_hosting': True,
        'feature_theme': True,
        'feature_icon': True,
        'feature_advanced_library': True,

        #
        # variants
        #
        'variants': {

            'yearly': {
                'name': 'Professional Plus Yearly',
                'price_eur': 350000,
                'price_usd': 425000,
                'price_gbp': 280000,
                'payment_interval': 'year',
                'value': 4003,
            },

            'monthly': {
                'name': 'Professional Plus Monthly',
                'price_eur': 34900,
                'price_usd': 39900,
                'price_gbp': 29900,
                'payment_interval': 'month',
                'value': 4002
            },

            'monthly-25-jobviddy': {
                'name': 'Professional Plus Monthly (25% Discount) Andy',
                'price_eur': 25900,
                'price_usd': 29900,
                'price_gbp': 22500,
                'payment_interval': 'month',
                'value': 4001,
                'subscribable': False,
                'feature_advanced_video_settings': True
            }
        }
    },

    # pro plan
    '201412-enterprise': {

        'group': 'enterprise',
        'subscribable': True,

        #
        # features
        #
        'feature_endscreen': True,
        'feature_advanced_settings': True,
        'feature_vimeo': True,
        'feature_wistia': True,
        'feature_custom_analytics': True,
        'feature_custom_hosting': True,
        'feature_theme': True,
        'feature_icon': True,
        'feature_advanced_library': True,

        #
        # variants
        #
        'variants': {

            'monthly': {
                'name': 'Enterprise Monthly',
                'price_eur': 129900,
                'price_usd': 139900,
                'price_gbp': 104900,
                'payment_interval': 'month',
                'value': 6001
            },

            'yearly': {
                'name': 'Enterprise Yearly',
                'price_eur': 1400000,
                'price_usd': 1500000,
                'price_gbp': 1000000,
                'payment_interval': 'year',
                'value': 6002
            }
        }
    },

    ###################
	# INDIVIDUAL
	###################

    'individual': {

        'group': 'individual',


        'variants': {

            'individual': {
                'name': 'Individual Plan',
                'price_eur': 0,
                'value': 8000
            },

            'meisterclass': {

                'name': 'Individual meisterclasss',

                'price_eur': 3500,
                'payment_interval': 'month',

                'feature_upload': False,
                'feature_endscreen': True,

                'value': 8001,
            },

            'escp': {
                'name': 'Individual escp',

                'price_eur': 3500,
                'payment_interval': 'month',

                'feature_endscreen': True,
                'feature_vimeo': True,
                'feature_upload': True,
                'feature_theme': True,
                'feature_advanced_library': True,

                'value': 8002,
            },

            'sspss': {

                'name': 'Individual SSPSS',

                'feature_vimeo': True,
                'feature_upload': True,
                'feature_endscreen': True,
                'feature_advanced_settings': True,
                'feature_wistia': True,
                'feature_theme': True,
                'feature_advanced_library': True,

                'value': 8003,
            },

            'agency-evaluation': {

                'name': 'Agency Evaluation',

                'feature_vimeo': True,
                'feature_upload': True,
                'feature_endscreen': True,
                'feature_advanced_settings': True,
                'feature_wistia': True,
                'feature_theme': True,
                'feature_icon': True,
                'feature_advanced_library': True,

                'value': 8004,
            },


            'staff': {
                'name': 'videopath staff account',

                # features
                'feature_vimeo': True,
                'feature_upload': True,
                'feature_endscreen': True,
                'feature_advanced_settings': True,
                'feature_wistia': True,
                'feature_dev': True,        
                'feature_custom_analytics': True,
                'feature_brightcove': True,
                'feature_custom_hosting': True,
                'feature_theme': True,
                'feature_icon': True,
                'feature_advanced_library': True,
                'feature_advanced_video_settings': True, 
                'feature_integrations': True,
                'feature_email_collector': True,
                'feature_teams': True,

                'value': 9999,
            }

        }
    }
}


DEFAULT_PLAN = 'free-free'

#
# Merge and flatten out variants
#
def _merge_variants(PLANS):
	result={}
	for plan_id, plan in PLANS.iteritems():
		for variant_id, variant in plan.pop('variants').iteritems():
			key = plan_id + '-' + variant_id
			result[key] = dict(PLAN_DEFAULTS.items()+plan.items() + variant.items() + [('id', key)])
	return result
PLANS = _merge_variants(PLANS)
PLANS_SORTED = sorted(PLANS.values(), key= lambda plan: plan["value"])
PLANS_CHOICES = map(lambda plan: (plan["id"], "{0:04d} {1} ({2})".format(plan["value"], plan["name"], plan["id"])), PLANS_SORTED)

#
# Set default
#
DEFAULT_PLAN = PLANS[DEFAULT_PLAN]

def SUBSCRIBABLE_PLANS(group):
	if group:
		return filter((lambda p: p["group"] == group and p["subscribable"] == True), PLANS.values())
	return filter((lambda p: p["subscribable"] == True), PLANS.values())


# test result
import pprint
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(PLANS)




