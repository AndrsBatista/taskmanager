from rest_framework import generics, viewsets, permissions
from .models import Task
from .serializers import TaskSerializer
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
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
    

@cache_page(60)
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.completed = True if request.POST.get('completed') == 'on' else False
        task.save()
        return redirect('home')

    return render(request, 'tasks/task_edit.html', {'task': task})


def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('home')


@cache_page(60)
def create_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        Task.objects.create(title=title, description=description)
        return redirect('home')
    
    return render(request, 'tasks/task_create.html')

@cache_page(60)  # Cache por 60 segundos
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/index.html', {'tasks': tasks})
