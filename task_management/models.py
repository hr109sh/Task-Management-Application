from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.

class TaskList(models.Model):
	username = models.ForeignKey(User, on_delete=models.CASCADE)
	task_name = models.CharField(max_length= 100)
	task_description = models.TextField()
	status = models.IntegerField(default=0)
	created_date = models.DateField(default=datetime.date.today)

	def __str__(self):
		return "%s %s" % (self.username, self.task_name)
