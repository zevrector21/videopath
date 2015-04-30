# configure plans
_plans_individual = {

    # individual plans
    'individual': {

        'group': 'individual',

        # features
        'max_projects': 9999,
        'max_views_month': 10000000,

        'value': 9999,

        'variants': {

            'individual': {
                'name': 'Individual Plan',
                'price_eur': 0,
                'payment_interval': 'month',
            },

            'lonelycaballero': {
                'name': 'Individual lonelycaballero',
                'price_eur': 2500,
                'payment_interval': 'month',

                'feature_upload': True,
                'feature_analytics': True,
                'feature_endscreen': True,
            },

            'meisterclass': {
            
                'name': 'Individual meisterclasss',
                'price_eur': 3500,
                'payment_interval': 'month',
                'feature_upload': False,
                'max_projects': 9999,

                'feature_analytics': True,
                'feature_endscreen': True,
                'feature_colors': True,
            },

            'escp': {
            
                'name': 'Individual escp',
                'price_eur': 3500,
                'payment_interval': 'month',
                'max_projects': 9999,

                'feature_analytics': True,
                'feature_endscreen': True,
                'feature_vimeo': True,
                'feature_upload': True,
                'feature_colors': True,

            },

            'sspss': {
                'name': 'Individual SSPSS',
                'feature_vimeo': True,
                'feature_upload': True,
                'feature_analytics': True,
                'feature_endscreen': True,
                'feature_colors': True,
                'feature_disable_share': True,
                'feature_equal_markers': True,
                'feature_wistia': True,
            },

            'agency-evaluation': {
                'name': 'Agency Evaluation',
                'feature_vimeo': True,
                'feature_upload': True,
                'feature_analytics': True,
                'feature_endscreen': True,
                'feature_colors': True,
                'feature_disable_share': True,
                'feature_equal_markers': True,
                'feature_wistia': True,
                'max_views_month': 500,
            },

            'staff': {
                'name': 'videopath staff account',
                'feature_vimeo': True,
                'feature_upload': True,
                'feature_analytics': True,
                'feature_endscreen': True,
                'feature_colors': True,
                'feature_disable_share': True,
                'feature_equal_markers': True,
                'feature_wistia': True,
                'feature_dev': True
            }

        }
    }

}