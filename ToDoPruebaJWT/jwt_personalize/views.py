# todos/views.py
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import MyTokenPersonalizeSerializer

class TokenPersonalizeView(TokenObtainPairView):
    serializer_class = MyTokenPersonalizeSerializer