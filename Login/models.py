from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
	address = models.CharField(max_length=100)
	phno = models.CharField(max_length=14)

	def __str__(self):
		return self.user.username
