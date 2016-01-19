
# configure plans
_plans_legacy = {


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