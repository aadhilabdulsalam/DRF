"""
URL configuration for employee_crud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from xml.etree.ElementInclude import include

from django.contrib import admin
from django.db import router
from django.urls import path,include
from employees import views
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('employees',views.EmployeeView)
urlpatterns = [

    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('search',views.SearchAPIView.as_view()),
    path('register',views.RegisterApiView.as_view()),
   # path('ed',views.EmployeeListCreate.as_view()),
    # path('ec',views.EmployeeCreate.as_view()),
    #path('ed/<int:pk>',views.EmployeeRetrieveUpdateDelete.as_view()),
    # path('de/<int:i>',views.EmployeeDelete.as_view()),
    # path('epu/<int:id>',views.EmployeeUpdate.as_view()),
    # path('eu/<int:pk>',views.EmployeepartialUpdate.as_view()),
    # path('er/<int:i>',views.EmployeeRetrieve.as_view()),
    # path('efu/<int:i>',views.EmployeeFullUpdate.as_view()),
    # path('epu/<int:i>',views.EmployeePartialUpdate.as_view()),
    # path('ed/<int:i>',views.EmployeeDelete.as_view()),

]
