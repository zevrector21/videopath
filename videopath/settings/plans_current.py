# configure plans
_plans_current = {

    # free plan, simple
    'free': {

        'group': 'free',
        'subscribable': True,

        'default': True,  # mark this as the default plan
        'value': 1000,

        # features
        'max_projects': 9999,
        'max_views_month': 2000,
        

        'variants': {
            'free': {
                'name': 'Free',
                'price_eur': 0,
                'price_usd': 0,
                'payment_interval': 'month',
            }
        }
    },


    # starter plan with 2 variants
    '201509-starter': {

        'group': 'starter',
        'subscribable': True,
        'feature_advanced_library': True,

        # features
        'max_projects': 9999,
        'max_views_month': 10000000,
        'feature_endscreen': True,

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

        # features
        'max_projects': 9999,
        'max_views_month': 10000000,
        'feature_endscreen': True,
        'feature_advanced_settings': True,
        'feature_vimeo': True,
        'feature_wistia': True,
        'feature_custom_analytics': True,
        'feature_custom_hosting': True,
        'feature_theme': True,
        'feature_icon': True,
        'feature_advanced_library': True,

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
            # individual monthly plans
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

        # features
        'max_projects': 9999,
        'max_views_month': 10000000,
        'feature_endscreen': True,
        'feature_advanced_settings': True,
        'feature_vimeo': True,
        'feature_wistia': True,
        'feature_custom_analytics': True,
        'feature_custom_hosting': True,
        'feature_theme': True,
        'feature_icon': True,
        'feature_advanced_library': True,

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


}

# configure coupons
_coupons_current = {

    #'coupon1' : {
    #   'plan' : 'starter-yearly',
    #   'price_eur' : 4000,
    #   'stripe_coupon_id' : '90percent'
    #},

    #'coupon2' : {
    #   'plan' : 'starter-yearly',
    #   'price_eur' : 20000,
    #   'stripe_coupon_id' : '50percent'
    #},

    #'coupon3' : {
    #   'plan' : 'starter-yearly',
    #   'price_eur' : 30000,
    #   'stripe_coupon_id' : '25percent'
    #},

    #'coupon4' : {
    #   'plan' : 'starter-yearly',
    #   'price_eur' : 36000,
    #   'stripe_coupon_id' : '10percent'
    #}

}