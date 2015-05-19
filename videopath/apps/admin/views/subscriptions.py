
from django.contrib.admin.views.decorators import staff_member_required
from django.template.response import SimpleTemplateResponse

from videopath.apps.admin.views import helpers
from videopath.apps.payments.models import Subscription
from django.conf import settings
import humanize


@staff_member_required
def view(request):

    # collect subscriptions
    result_array = []
    for sub in Subscription.objects.all().order_by("plan"):
        if sub.plan != settings.PLANS.default_plan["id"] and sub.user.username not in helpers.company_accounts:
            result_array.append([
                    helpers.userlink(sub.user),
                    sub.plan,
                    sub.managed_by,
                    sub.notes
                ])
    headers = ["User", "Plan", "Payment Method", "Notes"]
    result = helpers.table(result_array, headers)

    result += helpers.header("Plans")


    # collect Plans
    def renderplan( plan):

        features = ""
        for key, value in plan.iteritems():
            if "feature" in key:
                feature = key.replace("feature_", "").replace("_", " ") 
                if value:
                    feature = "<b>" + feature + "</b>"
                else:
                    feature = "<span style='color:gray'>" + feature + "</span>"
                features += feature + ", "
 
        result = [ "<b>" + plan["name"] + "</b><br />" + plan["id"], 
        humanize.intcomma(plan["price_usd"]/100), 
        humanize.intcomma(plan["price_eur"]/100), 
        humanize.intcomma(plan["max_views_month"]), 
        features,
        "x" if plan["subscribable"] else ""]
        return result

    array = []    
    for plan_id, plan in sorted(settings.PLANS.all_plans.iteritems()):
        array.append(renderplan(plan))
    result += helpers.table(array, ["Name", "USD", "EUR", "Views", "Features", "Subs."])


    return SimpleTemplateResponse("insights/base.html", {
        "title": "Subscriptions and Plans",
        "insight_content": result
        })
