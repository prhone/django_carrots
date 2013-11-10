from django.db import models
import datetime

class Poll(models.Model):
	question = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')

	def __str__(self):
		return self.question

	def recently_published(self):
		 a = datetime.datetime.now() - datetime.timedelta(days=1)
		 return self.pub_date >= a

class Choice(models.Model):
	poll = models.ForeignKey(Poll)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

	def __str__(self):
		return self.choice_text

# Create your models here.
