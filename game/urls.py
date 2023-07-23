from django.contrib import admin
from django.urls import path

from . import views

app_name = 'round'

urlpatterns = [

    path('', views.RoundsPlayed.as_view(), name='get_rounds'),
    path('<uuid:pk>/', views.GetRound.as_view(), name='get_round'),
    path('create', views.CreateRound.as_view(), name='create_round'),

    path('<uuid:pk>/invite', views.SendInvite.as_view(), name='send_invite'),
    path('reject/<uidb64>/<token>/', views.RejectInvite.as_view(), name='reject_invite'),
    path('accept/<uidb64>/<token>/', views.AcceptInvite.as_view(), name='accept_invite'),

]
