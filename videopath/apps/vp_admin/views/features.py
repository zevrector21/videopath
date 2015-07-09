
from django.contrib.admin.views.decorators import staff_member_required
from django.template.response import SimpleTemplateResponse
from django.db import connection

@staff_member_required
def view(request):






	# query const
	SELECT_DRAFT_REVISIONS = "SELECT COUNT(*) FROM videos_video as v JOIN videos_videorevision as vr ON(v.draft_id = vr.id)"
	USING_COLORS = "vr.ui_color_1 != '#424242'"

	cursor = connection.cursor()
	cursor.execute(SELECT_DRAFT_REVISIONS + " WHERE " + USING_COLORS)
	print cursor.fetchone()


	return SimpleTemplateResponse("insights/base.html", {
	    "title": "Features",
	    "insight_content": "Result"
	    })
