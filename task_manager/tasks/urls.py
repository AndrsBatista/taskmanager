from rest_framework import routers
from .views import TaskListCreate, TaskViewSet

router = routers.DefaultRouter()

router.register('api/app', TaskViewSet, 'tasks' )

urlpatterns = router.urls
