from videopath.apps.users.models import User


class EmailAuthBackend(object):

    def authenticate(self, username=None, password=None):
        """ Authenticate a user based on email address as the user name. """
        if not username:
            return None

        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        """ Get a User object from the user_id. """
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
