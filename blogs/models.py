from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BlogDataBase(models.Model):
	"""docstring for ClassName"""
	title		=models.CharField(max_length=100)
	author		=models.ForeignKey(User, on_delete=models.CASCADE)
	description	=models.TextField()

	def __str__(self):
		return f"{self.title}"

