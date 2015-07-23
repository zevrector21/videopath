import copy

from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

from videopath.apps.common.models import VideopathBaseModel
from videopath.apps.videos.managers.video_manager import VideoManager

class Video(VideopathBaseModel):

    # custom manager class
    objects = VideoManager()

    # constants
    PRIVATE = 0
    PUBLIC = 1
    PUBLISH_CHOICES = (
        (PRIVATE, 'Private'),
        (PUBLIC, 'Public'),
    )
    PLAYER_VERSION_CHOICES = (
        ("1", "1 - Scruffy"),
        ("2", "2 - Bender"),
        ("3", "3 - Zoidberg"),
        ("3", "3 - Zap Brannigan"),
    )

    # owner
    user = models.ForeignKey(User, related_name='videos')

    # public stuff
    key = models.CharField(
        max_length=50, blank=True, unique=True, db_index=True)
    published = models.IntegerField(default=PRIVATE, choices=PUBLISH_CHOICES)
    nice_name = models.CharField(max_length=50, blank=True, db_index=True)

    # revisions
    draft = models.OneToOneField(
        "VideoRevision", related_name="video_draft", blank=True, null=True, on_delete=models.SET_NULL)
    current_revision = models.OneToOneField(
        "VideoRevision", related_name="video_current", blank=True, null=True, on_delete=models.SET_NULL)

    # analytics
    total_plays = models.IntegerField(default=0)
    total_views = models.IntegerField(default=0)

    # code version
    player_version = models.CharField(
        max_length=20, choices=PLAYER_VERSION_CHOICES, default=settings.PLAYER_DEFAULT_VERSION)

    # define wether video is archived
    archived = models.BooleanField(default=False)


    def duplicate(self):

        # don't duplicate video with uploaded file
        if self.file.count() > 0:
            return None

        # create a copy of the draft
        duplicate = copy.copy(self)
        duplicate.pk = None
        duplicate.key = None

        # make sure we only have one revision as draft
        # and the video is marked as unpublished
        duplicate.draft = self.get_draft_or_current_revision().duplicate()
        duplicate.current_revision = None
        duplicate.published = 0

        # clean up some other values
        duplicate.total_plays = 0
        duplicate.total_views = 0
        duplicate.archived = False

        duplicate.save()

        # copy over video sources
        for source in self.video_sources.all():
            duplicate_source = source.duplicate()
            duplicate_source.video = duplicate
            duplicate_source.save()

        duplicate.draft.video = duplicate
        duplicate.draft.save()

        return duplicate

    # manage revisions/drafts
    def delete_draft(self):
        d = self.draft
        self.draft = None
        d.delete()

    def get_or_create_draft(self):
        if self.draft_id != None:
            return self.draft
        else:
            self.create_new_draft()
            return self.draft

    def get_draft_or_current_revision(self):
        if self.draft_id != None:
            return self.draft
        else:
            return self.current_revision

    def get_current_revision_or_draft(self):
        if self.current_revision_id != None:
            return self.current_revision
        else:
            return self.draft  

    def create_new_draft(self):
        if self.current_revision == None:
            return

        self.draft = self.current_revision.duplicate()
        self.save()

    # publish / unpublish
    def publish(self):
        if self.draft == None:
            return
        old_current_revision = self.current_revision
        self.current_revision = self.draft
        self.draft = None
        self.published = 1
        self.save()
        if old_current_revision != None:
            old_current_revision.delete()

        from videopath.apps.videos.util import video_export_util
        video_export_util.export_video(self)


    def unpublish(self):
        if self.current_revision == None:
            return
        if self.draft == None:
            self.draft = self.current_revision
            self.current_revision = None
        else:
            self.current_revision.delete()
            self.current_revision = None
        self.published = 0
        self.save()
        
        from videopath.apps.videos.util import video_export_util
        video_export_util.delete_export(self)



    # generate key on save
    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key(8)
        super(Video, self).save(*args, **kwargs)

    # name
    def __unicode__(self):
        return u'%s %s' % (self.key, self.user)

    # met stuff
    class Meta:
        app_label = "videos"

