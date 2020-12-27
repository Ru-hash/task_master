from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
class Task(models.Model):
	title = models.CharField(max_length=30)
	content = models.TextField()
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	def get_absolute_url(self):
		return reverse('tasks:TaskList')