from django.contrib import admin
from django.urls import path,include
from Api.views import CompanyviewSet,EmployeeviewSet
from rest_framework import routers

route = routers.DefaultRouter()
route.register(r'companies',CompanyviewSet)
route.register(r'employees',EmployeeviewSet)

urlpatterns = [
    path('',include(route.urls))
]