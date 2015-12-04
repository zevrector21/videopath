from django.contrib.auth.models import User
from django.conf import settings

from rest_framework import serializers

from videopath.apps.users.models import UserSettings, Team, TeamMember


class UserSettingsSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserSettings


class UserSerializer(serializers.ModelSerializer):

    plan = serializers.SerializerMethodField()
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


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('name', 'id')

class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMember
        fields = ('user')
