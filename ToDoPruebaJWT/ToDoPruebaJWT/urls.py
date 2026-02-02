# core/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from jwt_personalize.views import TokenPersonalizeView

urlpatterns = [
    path('admin/', admin.site.urls),

    # 1. Aquí conectamos la app de TODOS
    # Cualquier ruta que empiece con 'api/v1/' buscará dentro de todos.urls
    path('api/v1/', include('todo_app.urls')),
    

    path('api/token/', TokenPersonalizeView.as_view(), name='token_obtain_pair'),
    # El refresh se queda igual, ese no suele necesitar cambios
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]