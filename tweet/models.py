from django.db import models
from django.conf import settings
from django.utils.timezone import now

class Tweets(models.Model):
	tweet_id = models.AutoField(primary_key=True)
	username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	tweet = models.CharField(max_length=200)
	likes = models.IntegerField(default=0)
	date_created = models.DateTimeField(default=now)

class Hashtag_tweets(models.Model):
	hashtag = models.CharField(max_length=20)
	tweet_id = models.ForeignKey(Tweets, on_delete=models.CASCADE)
	count = models.IntegerField(default=0)

class Like_tweets(models.Model):
	username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	tweet_id = models.ForeignKey(Tweets, on_delete=models.CASCADE)