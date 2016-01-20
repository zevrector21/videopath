# configure plans
_plans_individual = {

    # individual plans
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