from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('home', views.HomeView.as_view(), name='home'),
    path('my_projects', views.ProjView.as_view(), name='my_projects'),
    path('my_projects/create', views.CreateProj.as_view(), name='my_projects_create'),
    path('my_project/<int:id>', views.DetailProject.as_view(), name='my_project'),
    path('my_project/<int:id>/update', views.UpdateProj.as_view(), name='my_project_update'),
    path('my_project/<int:id>/delete', views.DeleteProj.as_view(), name='my_project_delete'),
    path('my_project/<int:id>/create_task', views.CreateTask.as_view(), name='task_create'),
    path('my_project/task/<int:id>', views.DetailTask.as_view(), name='task'),
    path('my_project/task/<int:id>/update', views.UpdateTask.as_view(), name='task_update'),
    path('my_project/task/<int:id>/delete', views.DeleteTask.as_view(), name='task_delete'),
]
