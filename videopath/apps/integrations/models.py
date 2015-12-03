from django.db import models
from django.contrib.auth.models import User

from videopath.apps.users.models import Team

from videopath.apps.common.models import VideopathBaseModel


class Integration(VideopathBaseModel):

	# owner
    user = models.ForeignKey(User, related_name='integrations')
    team = models.ForeignKey(Team, related_name='integrations', null=True)

    SERVICE_CHOICES = (
    	('mailchimp', 'mailchimp'),
        ('vimeo', 'vimeo'),
        ('brightcove', 'brightcove')
    )

    service = models.CharField(max_length=255, default='', choices=SERVICE_CHOICES)

    # settings 
    credentials = models.CharField(max_length=2048, blank=True)
    settings = models.CharField(max_length=2048, blank=True)

    # meta settings
    class Meta:
        unique_together = ("user", "service")