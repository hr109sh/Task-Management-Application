"""agile URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('task_management.urls')),
    path('login/', views.login,{'template_name':'task_management/login.html'}, name='login'),
    path('logout/',views.logout, {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
]

admin.site.site_header = "Task Management"
admin.site.site_title = "Task Management"
admin.site.index_title = "Task Management"