from django.shortcuts import render
from rest_framework import viewsets
from kick_api.models import KickstarterCampaign
from kick_api.serializers import KickstarterSerializer
# Create your views here.

class KickStarterView(viewsets.ModelViewSet):
	queryset = KickstarterCampaign.objects.all()
	serializer_class = KickstarterSerializer