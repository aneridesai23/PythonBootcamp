from rest_framework import serializers
from kick_api.models import kickstarter

class kickstarterSerializer(serializers.ModelSerializer):
	class Meta:
		model = kickstarter
		fields = ('id', 'backers_count', 'blurb')

