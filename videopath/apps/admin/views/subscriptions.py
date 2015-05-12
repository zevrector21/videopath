
from django.contrib.admin.views.decorators import staff_member_required
from django.template.response import SimpleTemplateResponse

from videopath.apps.admin.views import helpers
from videopath.apps.payments.models import Subscription
from django.conf import settings



@staff_member_required
def view(request):

    result_array = []

    for sub in Subscription.objects.all().order_by("plan"):
        if sub.plan != settings.PLANS.default_plan["id"] and sub.user.username not in helpers.company_accounts:
            result_array.append([
                    helpers.userlink(sub.user),
                    sub.plan,
                    sub.managed_by
                ])

    headers = ["User", "Plan", "Payment Method"]
    return SimpleTemplateResponse("insights/base.html", {
        "title": "Subscriptions",
        "insight_content": helpers.table(result_array, headers)
        })
