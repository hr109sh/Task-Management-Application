from django.urls import path,include
from task_management import views
from rest_framework import routers
from django.views.generic import TemplateView

router = routers.DefaultRouter()
router.register('task_list',views.TaskView,basename="TaskView")

urlpatterns = [
	path('api-auth/', include('rest_framework.urls')),
	path('',include(router.urls)),
	path('task/', views.TaskUi.as_view(),name="task"),
]