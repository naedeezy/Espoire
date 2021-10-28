from django.db import models

# Create your models here.

class Transaction(models.Model):
	trans_type = models.CharField(max_length=200, null=True)
	number = models.CharField(max_length=200, null=True)
	amount = models.FloatField(null=True)
	name = models.CharField(max_length=200, null=True)
	trans_id = models.CharField(max_length=200, null=True)
	date = models.DateTimeField(auto_now_add=True, null=True, blank=True)



	def __str__(self):
		return self.name

#For Vodafone
#
#Transaction ID
#The amount involved
#Whether it was sent or received
#Means through which it was sent(MTN MOBILE MONEY,GT,etc)
#Date and time
#How much you were charged
#Your balance
#Your reference