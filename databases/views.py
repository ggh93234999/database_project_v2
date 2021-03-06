# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.models import User

from databases.models import *
from databases.serializers import *

from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.utils import timezone

# Create your views here.

def activate(request, uidb64, token):
    try:
        uid = uidb64
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class User_profilesViewSet(viewsets.ModelViewSet):
    queryset = User_profiles.objects.all()
    serializer_class = User_profilesSerializer

class EventsViewSet(viewsets.ModelViewSet):
    queryset = Events.objects.all()
    serializer_class = EventsSerializer

class TeamsViewSet(viewsets.ModelViewSet):
    queryset = Teams.objects.all()
    serializer_class = TeamsSerializer
    
    def update(self, request, pk=None):
        team = self.get_object()
        emails=[]
        request2 = request.data.copy()
        
        if request2.getlist('verify','false'):
            teamid = team.id
            da = Teammembers.objects.filter(team_id=teamid)
            se = TeammembersSerializer(da, many = True)
            for i in se.data:
                us = User.objects.get(pk=i['user_id'])
                emails.append(us.email)
            cnt = len(emails)
            event_id = request.data['event_id']
            event = Events.objects.get(pk = event_id)
            member_min = event.member_min
            member_max = event.member_max
            if cnt < member_min or member_max < cnt:
                request2['verify']='87'
                content = "the numbers of member must include %d and %d, your numbers of member is %d" % (member_min, member_max, cnt) 
                return Response(content, status = status.HTTP_400_BAD_REQUEST)

        serializer = TeamsSerializer(team, data = request2)

        if serializer.is_valid():
            serializer.save()
            content = "Hi team %s,\n\n you have registered Successfully.\n if you have any question about this please contact us\n email: nctudatabase@gmail.com\n" % (serializer.data['name'])
            if serializer.data['verify']:
                send_mail(
                    'event register accomplished',
                    content,
                    '<nctudatabase@gmail.com>',
                    emails
                )
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class TeammembersViewSet(viewsets.ModelViewSet):
    queryset = Teammembers.objects.all()
    serializer_class = TeammembersSerializer

class AnnouncementsViewSet(viewsets.ModelViewSet):
    queryset = Announcements.objects.all()
    serializer_class = AnnouncementsSerializer


