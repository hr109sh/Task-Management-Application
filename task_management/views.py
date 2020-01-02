from django.shortcuts import render
from rest_framework import viewsets
from task_management.models import TaskList
from task_management.serializers import TaskSerializer
from django.contrib.auth.models import User
from rest_framework import permissions
from django.views.generic import TemplateView
from django.views.generic.base import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required



#Create your views here.
class TaskView(viewsets.ModelViewSet):
	permission_classes = [permissions.IsAuthenticated]
	def get_queryset(self):
		user = User.objects.get(username= self.request.user)
		return TaskList.objects.filter(username = user).order_by('created_date')
	serializer_class = TaskSerializer


class TaskUi(View):
    @method_decorator(login_required)
    def get(self,request):
    	user = User.objects.get(username= self.request.user)
    	data = {
    		'user_id':user.id,
    		'username':self.request.user
    	}
    	return render(request,'task_management/index.html',context=data)







