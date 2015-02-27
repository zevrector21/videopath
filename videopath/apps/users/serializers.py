from django.contrib.auth.models import User
from django.conf import settings

from rest_framework import serializers

from videopath.apps.users.models import UserSettings


class UserSettingsSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserSettings


class UserSerializer(serializers.ModelSerializer):

    # settings = UserSettingsSerializer()
    plan = serializers.SerializerMethodField()
    # url = serializers.HyperlinkedIdentityField(view_name='user-detail')
    username = serializers.CharField(min_length=3, required=False)

    newsletter = serializers.BooleanField(required=False)

    password = serializers.CharField(min_length=6, required=False)
    new_password = serializers.CharField(min_length=6, required=False)

    def get_plan(self, user):
        plan = "free-free"
        try:
            plan = user.subscription.plan
        except:
            pass
        return settings.PLANS.plan_for_id(plan)

    class Meta:
        model = User
        fields = ('username', 'email', 'id', 'plan', 'url', 'new_password', 'password', 'newsletter')
        read_only_fields = ('username', 'id')
