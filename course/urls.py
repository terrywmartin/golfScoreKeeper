from django.contrib import admin
from django.urls import path

from . import views

app_name = 'course'

urlpatterns = [
    path('', views.CourseDescription.as_view(), name='course_description'),

]
