
from rest_framework.viewsets import ModelViewSet
from toDo.models import Tasks
from toDo.serializers import TaskSerializer


class TaskViewSet(ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializer
