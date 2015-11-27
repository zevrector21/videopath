
from django.contrib.auth.models import User
from videopath.apps.videos.models import Video


company_accounts = [
    "david",
    "product_demo", #company
    "marketing", # company
    "anna",
    "tim t", #tim 2
    "tim", # tim 1
    "trival", # thomas
    "nimaa", 
    "lcdenison", # louisa 1
    "dontdelete", # louisa 2
    "yana",
    "jolly",
    "junayd",
    "vp_test_basic",
    "vp_test_pro",
    "vp_test_enterprise",
]

non_paid_plans = [
	"free-free",
	"individual-staff",
	"individual-agency-evaluation"
]


#
# users
#
def all_users():
	viewset = User.objects.exclude(username__in=company_accounts)
	return viewset

def upgraded_users():
	viewset = all_users()
	viewset = viewset.exclude(subscription__isnull=True)
	viewset = viewset.exclude(subscription__plan__in=non_paid_plans)
	return viewset

def active_users():
	pass

#
# videos
#
def all_videos():
	viewset = Video.objects.exclude(user__username__in=company_accounts)
	return viewset

def published_videos():
	viewset = all_videos().filter(published=True)
	return viewset

def shared_videos():
	viewset = all_videos().filter(total_plays__gte=50)
	return viewset



