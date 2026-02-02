# todos/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TodoViewSet

# Creamos un router específico para ESTA app
router = DefaultRouter()
router.register(r'todos', TodoViewSet, basename='todo')

urlpatterns = [
    # Incluimos las rutas generadas por el router de esta app
    path('', include(router.urls)),
]