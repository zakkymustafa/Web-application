from django.db import models

# Create your models here.
class User(models.Model):
	# first_name=models.CharField(max_length=50)
	# second_name=models.CharField(max_length=50)
	your_name = models.CharField(max_length=50)
	email = models.EmailField(max_length=50)
	password = models.CharField(max_length=50)
	confirm_password = models.CharField(max_length=50)
	