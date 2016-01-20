execfile(os.path.join(SITE_ROOT, "settings/plans_current.py"))
execfile(os.path.join(SITE_ROOT, "settings/plans_individual.py"))
execfile(os.path.join(SITE_ROOT, "settings/plans_legacy.py"))

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
	'default': False,
	'subscribable': False,
	'group-alias': [],
	'max_projects': 9999,
    'max_views_month': 10000000,
    'name': 'None',
    'price_eur': 0,
    'price_usd': 0,
    'price_gbp': 0,
    'payment_interval': 'month',
    'value': 1
}

DEFAULT_PLAN = 'free-free'

PLANS = None


class _Plans():

	def __init__(self):

		self.default_plan = None
		self.all_plans = {}

		# flatten plans,
		# so variants are spread out like regular plans
		# store default plan in a variable
		plans = dict(_plans_current.items() + _plans_legacy.items() + _plans_individual.items())
		for plan_group in plans:
		    p = plans[plan_group]
		    for vname in p["variants"]:

		    	#name of the combined 
		    	npname = plan_group + "-" + vname

		    	# combine plan and variant
		        v = p["variants"][vname]
		        nplan = dict(PLAN_DEFAULTS.items()+p.items() + v.items())

		        # remove variant name
		        del[nplan["variants"]]

		        # add group and id
		        nplan["id"] = npname

		        # save
		        self.all_plans[npname] = nplan
		        if "default" in nplan and nplan["default"] == True:
		            self.default_plan = nplan



    # list all available plans
	def susbcribable_plans(self, name):
		if name:
			return filter((lambda p: p["group"] == name and p["subscribable"] == True), self.all_plans.values())
		return filter((lambda p: p["subscribable"] == True), self.all_plans.values())


	# fetch a plan by id
	def plan_for_id(self, plan_id, return_default=True):
	    for plan in self.all_plans.values():
	        if plan["id"] == plan_id:
	            return plan
	    return self.default_plan if return_default else None

	# get a list of subscription choices for database
	def model_subscription_choices(self):
	    sorted_plans = self.all_plans.values()
	    sorted_plans.sort(key= lambda plan: plan["value"])
	    choices = []
	    for plan in sorted_plans:
	        name = "{0:04d} {1} ({2})".format(plan["value"], plan["name"], plan["id"])
	        choices.append((plan["id"], name))
	    return choices

PLANS = _Plans()


