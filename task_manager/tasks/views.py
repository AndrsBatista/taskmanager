from rest_framework import generics
from .models import Task
from rest_framework import viewsets, permissions
from .serializers import TaskSerializer
from django.http import JsonResponse

def home(request):
    return JsonResponse({"message": "Welcome to Task Manager API!"})


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
