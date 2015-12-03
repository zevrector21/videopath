import random
import string

from django.contrib.auth.models import User
from django.db.models import Q
from django.conf import settings

from userena.models import UserenaSignup

from rest_framework import status
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes
from rest_framework.exceptions import ValidationError, PermissionDenied
from rest_framework.response import Response
from rest_framework.decorators import api_view

from videopath.apps.common.services import service_provider
from videopath.apps.users.models import AuthenticationToken, OneTimeAuthenticationToken, UserCampaignData
from videopath.apps.users.serializers import UserSerializer
from videopath.apps.common.mailer import send_signup_email, send_forgot_pw_mail
from videopath.apps.users.permissions import UserPermissions

from videopath.apps.users.actions import login_user


#
# testing ip
#
@api_view(['GET'])
@permission_classes((AllowAny,))
def ip_check(request):
    service = service_provider.get_service("geo_ip")
    return Response(service.record_from_request(request));

#
# "Login" and "Logout" methods
#
@api_view(['POST', 'DELETE'])
@permission_classes((AllowAny,))
def api_token(request):
    
    # logout    
    if request.method == "DELETE":
        if not request.user.is_authenticated():
            raise PermissionDenied
        AuthenticationToken.objects.get(key=request.auth).delete()
        return Response()

    # get token
    if request.method == "POST":
        username = request.data.get("username", "").lower()
        password = request.data.get("password", "")
        user, token, ottoken = login_user.run(username, password)    
        if token:
            serializer = UserSerializer(user, context={'request': request})
            return Response({
                'api_token': token.key, 
                'user': serializer.data, 
                'api_token_once': ottoken.key
            })
        else:
            raise PermissionDenied

#
# Generate a new password and send an email
#
@api_view(['POST'])
@permission_classes((AllowAny,))
def password_reset(request):

    name = request.data.get("username", None).lower()
    try:
        user = User.objects.get(Q(username=name) | Q(email=name))
    except User.DoesNotExist or User.MultipleObjectsReturned:
        raise ValidationError(detail="Could not find user.")

    # create new pw
    password = ''.join(random.choice(
        string.ascii_uppercase + string.digits + string.ascii_lowercase) for x in range(12))
    user.set_password(password)
    user.save()
    send_forgot_pw_mail(user, password)

    return Response(status=201)


#
# Rest framework user view set
#
class UserViewSet(viewsets.ModelViewSet):

    model = User
    serializer_class = UserSerializer
    permission_classes = (UserPermissions,)

    # Can see only yourself
    def get_queryset(self):
        return User.objects.filter(pk=self.request.user.pk)

    def perform_update(self, serializer):
        instance = serializer.save()

        # if there is a new password,
        # set that on the user
        new_password = self.request.data.get("new_password")
        if new_password:
            instance.set_password(new_password)
            instance.save()

    #
    # Custom create method, pluggin in userena
    #
    def create(self, request, *args, **kwargs):

        # get and validate data
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data.get("username").lower()
        email = serializer.validated_data.get("email").lower()
        password = serializer.validated_data.get("password")

        if len(username) <= 3:
            raise ValidationError(detail={"username":["Username must be a least 3 characters."]})
        if len(email) == 0:
            raise ValidationError(detail={"email":["Please supply a valid email address"]})

        if User.objects.filter(email__iexact=email).count() > 0:
           raise ValidationError(detail={"email":["Email is taken."]})
        if User.objects.filter(username__iexact=username).count() > 0:
           raise ValidationError(detail={"username":["Username is taken."]})

        # create via userena
        user = UserenaSignup.objects.create_user(username[:30],
                                     email,
                                     password,
                                     active=True, send_email=False)
       

        # send a signup email
        send_signup_email(user)

        # users geo record
        geo_service = service_provider.get_service("geo_ip")
        geo_record = geo_service.record_from_request(request)

        # create campaign information if available
        campaign_data = UserCampaignData.objects.create(user=user)
        campaign_data.country = geo_record['country_full'][:500]

        if request.data:

            try:
                campaign_data.referrer = request.data.get('referrer', '')[:500]
            except: pass

            campaign = request.data.get('campaign', {})
            if campaign:
                try:
                    campaign_data.source = campaign.get('source', '')[:500]
                    campaign_data.medium = campaign.get('medium', '')[:500]
                    campaign_data.name = campaign.get('name', '')[:500]
                    campaign_data.content = campaign.get('content', '')[:500]
                    campaign_data.term = campaign.get('term', '')[:500]
                except: pass
        
        campaign_data.save()

        # subscribe to mailchimp if they want to
        if serializer.validated_data.get("newsletter", False):
            try:
                email = user.email  
                service = service_provider.get_service("mailchimp")      
                service.subscribe_email(email)      
            except: pass

        # create tokens
        token = AuthenticationToken.objects.create(user=user)
        ottoken = OneTimeAuthenticationToken.objects.create(token=token)
        

        # greate britain
        if geo_record["country"] in ["UK", "GB"]:
            user.settings.currency = settings.CURRENCY_GBP
        # rest of europe
        elif geo_record["continent"] == "EU":
            user.settings.currency = settings.CURRENCY_EUR
        # rest of world
        else:
            user.settings.currency = settings.CURRENCY_USD

        try:
            user.settings.phone_number = request.data.get('phone', '')
        except: pass

        user.settings.save()

        # create response
        data = UserSerializer(user, context={'request': request}).data
        data["api_token"] = token.key
        data["api_token_once"] = ottoken.key

        slack = service_provider.get_service("slack")
        slack.notify("User " + user.email + " just signed up from " + geo_record["country_full"] + ".")

        # possibly return some tokens and shit
        return Response(data, status=status.HTTP_201_CREATED)

    
