from rest_framework import generics, viewsets, permissions
from .models import Task
from .serializers import TaskSerializer
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.core.cache import cache  # ✅ SOLO este import

def home(request):
    return JsonResponse({"message": "Task Manager API"})

# Vista de prueba para verificar que Redis funciona
def test_cache_view(request):
    cache.set('my_key', 'my_value', timeout=None)
    value = cache.get('my_key')
    return JsonResponse({"cached_value": value})

class TaskListCreate(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TaskSerializer

@cache_page(60)  # Cache por 60 segundos
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/index.html', {'tasks': tasks})
