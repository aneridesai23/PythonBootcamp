from django.shortcuts import render
from django.http import HttpResponse
from kickAPI.models import KickstarterCampaign
from django.core import serializers

# Create your views here.
def getKickstarterCampaign(request, kickstarterID):
	kickstarterID = KickstarterCampaign.objects.filter(id = kickstarterID)
	data = serializers.serialize("json", KickstarterCampaign.objects.all())
	print(KickstarterCampaign.objects.all())
	return HttpResponse(data)
