# todos/views.py
from rest_framework import viewsets
from .models import Todo
from .serializers import TodoSerializer

from django.contrib.admin.models import LogEntry, ADDITION, CHANGE, DELETION
from django.contrib.contenttypes.models import ContentType

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

        # 1. Guardamos el objeto real
        instance = serializer.save()
        
        # 2. Creamos el registro en la bitácora (LogEntry)
        LogEntry.objects.log_action(
            user_id=self.request.user.id,
            content_type_id=ContentType.objects.get_for_model(instance).pk,
            object_id=instance.pk,
            object_repr=str(instance),
            action_flag=ADDITION,  # Bandera de "Agregado"
            change_message="Creado desde la API"
        )

    def perform_update(self, serializer):
        instance = serializer.save()
        
        LogEntry.objects.log_action(
            user_id=self.request.user.id,
            content_type_id=ContentType.objects.get_for_model(instance).pk,
            object_id=instance.pk,
            object_repr=str(instance),
            action_flag=CHANGE,  # Bandera de "Modificado"
            change_message="Actualizado desde la API"
        )

    def perform_destroy(self, instance):
        # Guardamos datos antes de borrar porque luego instance.pk puede perderse o dar error
        content_type_id = ContentType.objects.get_for_model(instance).pk
        object_id = instance.pk
        object_repr = str(instance)

        # Borramos el objeto
        instance.delete()

        # Registramos que se borró
        LogEntry.objects.log_action(
            user_id=self.request.user.id,
            content_type_id=content_type_id,
            object_id=object_id,
            object_repr=object_repr,
            action_flag=DELETION,  # Bandera de "Eliminado"
            change_message="Borrado desde la API"
        )
    
    
