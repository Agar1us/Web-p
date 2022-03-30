from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('home', views.HomeView.as_view(), name='home'),
    path('create_post', views.CreatePostView.as_view(), name='create_post'),
    path('post/<int:id>/', views.PostView.as_view(), name='post'),
]
