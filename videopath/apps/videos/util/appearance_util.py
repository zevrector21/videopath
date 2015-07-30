from django.conf import settings

#
# Inject appearance info
#
import shlex
def appearance_for_revision(revision):

    from videopath.apps.videos.models import PlayerAppearance
    from videopath.apps.videos.serializers import PlayerAppearanceSerializer

    def convert(s): # convert string to dict
        return dict(token.split('=') for token in shlex.split(s))

   # build appearance in the right order
    result = settings.DEFAULT_VIDEO_APPEARANCE.copy()
    user = revision.video.user

    # merge appearance from model on user 
    try:
        vrs = PlayerAppearanceSerializer(user.default_player_appearance)
        result.update(vrs.data)  
    except PlayerAppearance.DoesNotExist:
        pass

    # merge appearance from model on revision
    try:
        if revision.player_appearance:
            vrs = PlayerAppearanceSerializer(revision.player_appearance)
            result.update(vrs.data)  
    except PlayerAppearance.DoesNotExist:
        pass

    # can be removed after frontend migration
    result["icon"] = result.get("ui_icon", None)
    result["icon_link_target"] = result.get("ui_icon_link_target", None)
    result["language"] = result.get("ui_language", None)

    return result