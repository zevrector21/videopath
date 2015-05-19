execfile(os.path.join(SITE_ROOT, "settings/plans_current.py"))
execfile(os.path.join(SITE_ROOT, "settings/plans_individual.py"))
execfile(os.path.join(SITE_ROOT, "settings/plans_legacy.py"))


class _Plans():

	# default entries of any plan
	reset_plan= {

		'default': False,
		'subscribable': False,

		# features for reference
		'feature_upload': False,
		'feature_analytics': False,
		'feature_endscreen': False,
		'feature_vimeo': False,
		'feature_colors': False,
		'feature_dev': False,
		'feature_disable_share': False,
		'feature_equal_markers': False,
        'feature_wistia': False,

		'max_projects': 9999,
        'max_views_month': 2000,

        'name': 'None',
        'price_eur': 0,
        'price_usd': 0,
        'payment_interval': 'month',

        'value': 1
	}

	def __init__(self):

		self.default_plan = None
		self.coupons = _coupons_current;
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
		        nplan = dict(self.reset_plan.items()+p.items() + v.items())

		        # remove variant name
		        del[nplan["variants"]]

		        # add group and id
		        nplan["id"] = npname

		        # save
		        self.all_plans[npname] = nplan
		        if "default" in nplan and nplan["default"] == True:
		            self.default_plan = nplan


		# merge plans into coupons
		for ckey in self.coupons:
		    c = self.coupons[ckey]
		    self.coupons[ckey] = dict(self.all_plans[c["plan"]].items() + c.items())
		    self.coupons[ckey]["id"] = ckey


    # list all available plans
	def susbcribable_plans(self, name):

		if name:
			result = filter((lambda p: p["group"] == name and p["subscribable"] == True), self.all_plans.values())
			result += filter(lambda c: c["id"] == name, self.coupons.values())
		else:
			result = filter((lambda p: p["subscribable"] == True), self.all_plans.values())
		return result


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


