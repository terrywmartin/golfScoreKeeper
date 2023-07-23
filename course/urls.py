from django.contrib import admin
from django.urls import path

from . import views

app_name = 'course'

urlpatterns = [
    path('', views.GetCourses.as_view(), name='get_courses'),
    path('<uuid:pk>/', views.GetCourse.as_view(), name='get_course'),
    path('create/', views.CreateCourse.as_view(), name='create_course'),
    path('<uuid:pk>/edit/', views.EditCourse.as_view(), name='edit_course'),
    path('<uuid:pk>/delete/', views.DeleteCourse.as_view(), name='delete_course'),

    path('<uuid:pk>/preview', views.PreviewCourse.as_view(), name='preview_course'),

    path('<uuid:pk>/holes', views.GetHoles.as_view(), name='get_holes'),
    path('<uuid:pk>/holes/<uuid:holeId>/', views.GetHole.as_view(), name='get_hole'),
    path('<uuid:pk>/holes/<uuid:holeId>/edit', views.EditHole.as_view(), name='edit_hole'),
    path('<uuid:pk>/holes/<uuid:holeId>/delete', views.DeleteHole.as_view(), name='delete_hole'),
    path('<uuid:pk>/holes/create', views.CreateHole.as_view(), name='create_hole'),

]
