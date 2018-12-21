from rest_framework import serializers
from kick_api.models import KickstarterCampaign

class KickstarterSerializer(serializers.ModelSerializer):
	class Meta:
			model = KickstarterCampaign
			fields = ('id', 'backers_count', 'blurb')
			'''
			'category', 'converted_pledge_amount',
			'country', 'created_at', 'creator', 'currency', 'curreny_symbol', 'currency_trailing_code',
			'current_currency', 'deadline', 'disable_communication', 'friends', 'fx_rate', 'goal', 'kickstarter_id',
			'is_backing', 'is_starrable', 'is_starred', 'launched_at', 'location', 'name', 'permissions', 'photo', 
			'pledged', 'profile', 'slug', 'source_url', 'spotlight', 'staff_pick', 'state', 'state_changed_at',
			'static_usd_rate', 'urls', 'usd_pledged', 'usd_type')
			'''