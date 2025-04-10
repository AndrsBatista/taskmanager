from rest_framework import routers
from django.urls import path, include
from .views import TaskListCreate, TaskViewSet, task_list, create_task
from . import views

router = routers.DefaultRouter()
router.register('api/app', TaskViewSet, 'tasks')

urlpatterns = [
    # Incluir las rutas del router para la API REST
    path('', include(router.urls)),
    
    # Ruta para la vista basada en templates
    path('', task_list, name='task_list'),
    path('task/new/', create_task, name='create_task'),
    path('tasks/<int:task_id>/delete/', views.delete_task, name='delete_task'),
    path('tasks/<int:task_id>/edit/', views.edit_task, name='edit_task'),



]


