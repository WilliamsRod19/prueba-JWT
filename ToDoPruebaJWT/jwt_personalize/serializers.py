from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class MyTokenPersonalizeSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # AQUI agregas cosas DENTRO del token encriptado
        # (Esto se ve si decodificas el token en jwt.io)
        token['username'] = user.username

        return token

    # # OPCIONAL: Si quieres modificar la respuesta JSON que recibe el Postman/Frontend
    # # (Para no tener que decodificar el token para ver el nombre)
    # def validate(self, attrs):
    #     data = super().validate(attrs)

    #     # Aquí agregas datos extras a la respuesta JSON directa
    #     data['nombre_usuario'] = self.user.username
    #     data['mensaje'] = '¡Login exitoso, crack!'
        
    #     return data