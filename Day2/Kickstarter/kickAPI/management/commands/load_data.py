import csv
from django.core.management import BaseCommand
from datetime import datetime
from django.utils import timezone
from kickAPI.models import KickstarterCampaign

class Command(BaseCommand):

	def add_arguments(self, parser):
		parser.add_argument('--path', type=str)

	def handle(self, *args, **kwargs):
		path = kwargs['path']
		KickstarterCampaign.objects.all().delete()
		with open(path, 'rt', encoding='utf-8') as csv_file:
			csv_reader = csv.reader(csv_file, dialect='excel')
			for row in csv_reader:
				campaign = KickstarterCampaign.objects.create(
						backers_count = row[0],
						blurb = row[1],
						category = row[2], 
						converted_pledged_amount = row[3],
						country = row[4],
						created_at = row[5],
						creator = row[6],
						currency = row[7],
						deadline = row[8],
						disable_communication = row[9],
						fx_rate = row[10],
						goal = row[11],
						kickstarterid = row[12],
						launched_at = row[13],
						location = row[14],
						name = row[15],
						photo = row[16],
						pledged = row[17],
						profile = row[18],
						slug = row[19],
						source_url = row[20],
						spotlight = row[21],
						staff_pick = row[22],
						state = row[23],
						state_changed_at = row[24],
						static_usd_rate = row[25],
						urls = row[26],
						usd_pledged = row[27],
						usd_type = str(row[28])
					)
			#	line_count =+ 1
		