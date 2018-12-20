from django.shortcuts import render
from rest_framework import viewsets
from kick_api.models import kickstarter
from kick_api.serializers import kickstarterSerializer

class kickStarterView(viewsets.ModelViewSet):
	queryset = kickstarter.objects.all()
	serializer_class = kickstarterSerializer
