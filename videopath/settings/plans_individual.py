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
                'feature_endscreen': True,
            },

            'meisterclass': {
            
                'name': 'Individual meisterclasss',
                'price_eur': 3500,
                'payment_interval': 'month',
                'feature_upload': False,
                'max_projects': 9999,

                'feature_endscreen': True,
            },

            'escp': {
            
                'name': 'Individual escp',
                'price_eur': 3500,
                'payment_interval': 'month',
                'max_projects': 9999,

                'feature_endscreen': True,
                'feature_vimeo': True,
                'feature_upload': True,
                'feature_theme': True,
                'feature_advanced_library': True,
                
            },

            'sspss': {
                'name': 'Individual SSPSS',
                'feature_vimeo': True,
                'feature_upload': True,
                'feature_endscreen': True,
                'feature_advanced_settings': True,
                'feature_wistia': True,
                'feature_theme': True,
                'feature_advanced_library': True
            },

            'agency-evaluation': {
                'name': 'Agency Evaluation',
                'feature_vimeo': True,
                'feature_upload': True,
                'feature_endscreen': True,
                'feature_advanced_settings': True,
                'feature_wistia': True,
                'max_views_month': 500,
                'feature_theme': True,
                'feature_icon': True,
                'feature_advanced_library': True,

            },

            'nyia': {
                'name': 'Nyia Personal Plan',
                'feature_vimeo': True,
                'feature_upload': True,
                'feature_endscreen': True,
                'feature_advanced_settings': True,
                'feature_wistia': True,
                'max_views_month': 500,
                'price_eur': 2000,
                'payment_interval': 'month',
            },

            'mediacrax': {
                'name': 'Mediacrax Plan',
                'feature_vimeo': True,
                'feature_upload': True,
                'feature_endscreen': True,
                'feature_advanced_settings': True,
                'feature_wistia': True,
                'max_views_month': 50000,
                'price_eur': 18900,
                'payment_interval': 'month',
                'feature_theme': True,
                'feature_advanced_library': True,

            },

            'staff': {
                'name': 'videopath staff account',
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
                'feature_email_collector': True
            }

        }
    }

}