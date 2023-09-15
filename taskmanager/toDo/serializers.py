from rest_framework.serializers import ModelSerializer
from toDo.models import Tasks


class TaskSerializer(ModelSerializer):
    class Meta:
        model = Tasks
        fields = '__all__'

