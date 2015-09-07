
# configure plans
_plans_legacy = {

     # starter plan with 2 variants
    '201410-starter': {

        'group': 'starter',


        # features
        'max_projects': 9999,
        'max_views_month': 15000,
        'feature_analytics': True,
        'feature_endscreen': True,
        'feature_theme': True,

        'variants': {
            'yearly': {
                'name': 'Basic Yearly',
                'price_eur': 16500,
                'payment_interval': 'year',
                'value': 11,
            },
            'monthly': {
                'name': 'Basic Monthly',
                'price_eur': 1500,
                'payment_interval': 'month',
                'value': 10,
            }
        }

    },

        # starter plan with 2 variants
    '201412-starter': {

        'group': 'starter',
        'subscribable': False,

        # features
        'max_projects': 9999,
        'max_views_month': 10000000,
        'feature_endscreen': True,
        'feature_vimeo': True,
        'feature_wistia': True,
        'feature_advanced_settings': True,
        'feature_theme': True,


        'variants': {
            'yearly': {
                'name': 'Basic Yearly',
                'price_eur': 80000,
                'price_usd': 100000,
                'price_gbp': 65000,
                'payment_interval': 'year',
                'value': 11,
            },
            'monthly': {
                'name': 'Basic Monthly',
                'price_eur': 7900,
                'price_usd': 9900,
                'price_gbp': 5900,
                'payment_interval': 'month',
                'value': 10,
            }
        }

    },
    
}