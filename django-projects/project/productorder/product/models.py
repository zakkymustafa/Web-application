from django.db import models
from user.models import User

# Create your models here.

class Product(models.Model):
	product_name=models.CharField(max_length=50)
	product_description=models.TextField()
	product_image=models.ImageField()
	user=models.ForeignKey(User,on_delete=models.PROTECT)

	def __str__(self):
		return self.product_name
	


