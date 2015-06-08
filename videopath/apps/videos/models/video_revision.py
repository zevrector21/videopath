import copy
from hashlib import sha256

from django.db import models

from videopath.apps.common.models import VideopathBaseModel, ColorField
from videopath.apps.videos.models import Video, PlayerAppearance

class VideoRevision(VideopathBaseModel):

    video = models.ForeignKey(Video, related_name="revisions")

    title = models.CharField(max_length=255, default="New Video")

    # images (should actually be defined in the files module, works better
    # with a foreign relationship key in this case though)
    custom_thumbnail = models.ForeignKey(
        "files.ImageFile", related_name="video_thumbnail", blank=True, default=None, null=True)

    # model can either be attached to a video revision or
    player_appearance = models.ForeignKey(PlayerAppearance, 
                                            blank=True,
                                            null=True,
                                            default=None,
                                            on_delete=models.SET_NULL,
                                            related_name="video_revisions")

    # meta
    description = models.TextField(blank=True)

    # custom configs
    # TODO merge into new appearance model
    video_appearance = models.TextField(blank=True)

    # custom google analytics tracking code
    custom_tracking_code = models.CharField(max_length=20, blank=True)

    # ui color
    ui_color_1 = ColorField(default="#424242")
    ui_color_2 = ColorField(default="#ffffff")

    # other ui settings
    ui_disable_share_buttons = models.BooleanField(default=False)
    ui_equal_marker_lengths = models.BooleanField(default=False)
    ui_fit_video = models.BooleanField(default=False)

    # iphone support
    iphone_images = models.IntegerField(default=-1)
    
    # endscreen settings
    endscreen_url = models.CharField(max_length=512, blank=True)
    endscreen_title = models.CharField(max_length=512, blank=True)
    endscreen_background_color = ColorField(default="#32526e", blank=True)
    endscreen_button_title = models.CharField(
        default="Try videopath now", max_length=512, blank=True)
    endscreen_button_target = models.CharField(
        default="http://videopath.com", max_length=512, blank=True)
    endscreen_button_color = ColorField(default="#ff6b57", blank=True)
    endscreen_subtitle = models.CharField(
        default="Create your own interactive video", max_length=512, blank=True)


    # password protection
    password = models.CharField(max_length=512, blank=True) # stores the salted sha digest
    password_hashed = models.CharField(max_length=512, blank=True) # helper field for updateing the password
    password_salt = models.CharField(max_length=512, blank=True) # stores the salt specific to this video

    # @property
    # def password(self):
    #     return self._password

    # @password.setter
    # def password(self, password):

    #     if not password:
    #         return

    #     if password == self._password:
    #         return

    #     if password == "clear":
    #         self._password = ""
    #         return

    #     # generate salt if not present
    #     if not self.password_salt:
    #         self.password_salt = self.generate_key(32)
    #     # save salted password
    #     self._password = sha256(password+self.password_salt).digest()

    def pre_save(self):
        print "pre_save"
        pass

    def save(self, *args, **kwargs):
        
        if not self.password_salt:
            self.password_salt = self.generate_key(32)

        if self.password and self.password !=self.password_hashed:
            self.password_hashed = unicode(sha256(self.password+self.password_salt).hexdigest())

        self.password = self.password_hashed


        super(VideoRevision, self).save(*args, **kwargs)


    # duplicate the revision
    def duplicate(self):

        # create a copy of the draft
        duplicate = copy.copy(self)
        duplicate.pk = None
        duplicate.save()

        # also dupicate all markers
        for marker in self.markers.all():
            dup_marker = marker.duplicate()
            dup_marker.video_revision = duplicate
            dup_marker.save()

        return duplicate

    def __unicode__(self):
        return "Revision " + str(self.id) + " - " + self.video.key

    class Meta:
        app_label = "videos"

