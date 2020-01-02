from rest_framework import serializers
from task_management.models import TaskList

class TaskSerializer(serializers.ModelSerializer):
	class Meta:
		model = TaskList
		fields = ('id','username','task_name','task_description','status')
