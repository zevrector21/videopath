
from videopath.apps.videos.models import Video, PlayerAppearance
from videopath.apps.common.test_utils import BaseTestCase

from videopath.apps.videos.util import appearance_util

# Uses the standard django frame testing client
class TestCase(BaseTestCase):

    def setup(self):
        self.create_user()

    def test_appearances_model(self):
        
        # test default appearance settings
        video = Video.objects.create(user=self.user)

        # default lang is english
        app = appearance_util.appearance_for_revision(video.draft)
        self.assertEqual(app.get("language"), "en")

        # set default user
        video.user.default_player_appearance = PlayerAppearance.objects.create(language="de")
        video.draft.save()
        app = appearance_util.appearance_for_revision(video.draft)
        self.assertEqual(app.get("language"), "de")

        # set video
        video.draft.player_appearance = PlayerAppearance.objects.create(language="fr")
        video.draft.save()
        app = appearance_util.appearance_for_revision(video.draft)
        self.assertEqual(app.get("language"), "fr")
