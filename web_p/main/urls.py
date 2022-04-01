from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('home', views.HomeView.as_view(), name='home'),
    path('project/<int:id>/create_invention/', views.CreateInvitation.as_view(), name='create_invention'),
    path('invitation/list/', views.ListInvitation.as_view(), name='list_invitation'),
    path('invitation/<int:id>/delete/', views.DeleteInvitation.as_view(), name='delete_invitation'),
    path('invitation/<int:id>/accept/', views.AcceptInvitation.as_view(), name='accept_invitation'),
]

