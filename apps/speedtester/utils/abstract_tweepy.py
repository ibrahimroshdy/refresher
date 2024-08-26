import tweepy
import os

import django
import speedtest
from django.db.utils import IntegrityError
from loguru import logger
import pytz
from django.db.models import Avg, Max, Min, Sum

# Setup django to be able to access the settings file
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'refresher_config.settings')
django.setup()

from apps.speedtester.models import ServersModel, SpeedtesterModel

# auth = tweepy.Client(
#         bearer_token="",
#         consumer_key="",
#         consumer_secret="",
#         access_token="",
#         access_token_secret="")
#
# auth.create_tweet(text="First automated tweet via refresher")

from datetime import datetime, timedelta, time

today = datetime.now()
tomorrow = today + timedelta(1)
today_start = datetime.combine(today, time())
today_end = datetime.combine(tomorrow, time())

objs = SpeedtesterModel.objects.filter(created__lte=today_end, created__gte=today_start)
print(objs.aggregate(Avg('download'), Avg('upload')))
print(objs.aggregate(Max('download'), Max('upload')))
print(objs.aggregate(Min('download'), Min('upload')))

