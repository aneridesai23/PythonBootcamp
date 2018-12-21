from django.db import models
# Create your models here.

class KickstarterCampaign(models.Model):
    backers_count=models.IntegerField()
    blurb=models.TextField()
    category=models.TextField()
    converted_pledged_amount=models.IntegerField()
    country=models.TextField()
    created_at=models.IntegerField()
    creator=models.TextField()
    currency=models.TextField()
    currency_symbol=models.TextField()
    currency_trailing_code=models.TextField()
    current_currency=models.TextField()
    deadline=models.IntegerField()
    disable_communication=models.TextField()         # was boolean
    friends=models.TextField()
    fx_rate=models.FloatField()
    goal=models.FloatField()
    kickstarter_id=models.IntegerField()
    is_backing=models.TextField()
    is_starrable=models.TextField()                  # was boolean
    is_starred=models.TextField()
    launched_at=models.IntegerField()
    location=models.TextField()
    name=models.TextField()
    permissions=models.TextField()
    photo=models.TextField()
    pledged=models.FloatField()
    profile=models.TextField()
    slug=models.TextField()
    source_url=models.URLField()
    spotlight=models.TextField()                     # was boolean
    staff_pick=models.TextField()                    # was boolean
    state=models.TextField()
    state_changed_at=models.IntegerField()
    static_usd_rate=models.FloatField()
    urls=models.TextField()
    usd_pledged=models.FloatField()
    usd_type=models.TextField()

    class Meta:
        ordering = ['backers_count']