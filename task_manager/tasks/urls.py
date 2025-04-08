from rest_framework import routers
from django.urls import path, include
from .views import TaskListCreate, TaskViewSet, task_list

router = routers.DefaultRouter()
router.register('api/app', TaskViewSet, 'tasks')

urlpatterns = [
    # Incluir las rutas del router para la API REST
    path('', include(router.urls)),
    
    # Ruta para la vista basada en templates
    path('', task_list, name='task_list'),
]


