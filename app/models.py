from django.db import models


# Create your models here.
class User(models.Model):
	firstName = models.CharField(max_length=192)
	lastName = models.CharField(max_length=192)
	email = models.EmailField(max_length=254)

	def __str__(self):
		return f'{self.firstName} {self.lastName}'