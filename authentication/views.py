"""
Vues d'authentification API
"""

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

from drf_spectacular.utils import extend_schema


class LoginAPIView(APIView):
    """
    Vue de connexion API (Token)
    """

    @extend_schema(
        request={
            "application/json": {
                "type": "object",
                "properties": {
                    "username": {"type": "string"},
                    "password": {"type": "string"},
                },
                "required": ["username", "password"],
            }
        },
        responses={
            200: {
                "type": "object",
                "properties": {
                    "token": {"type": "string"}
                }
            }
        },
        description="Connexion utilisateur et récupération du token"
    )
    def post(self, request):
        """
        Authentifie un utilisateur et retourne son token
        """
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)

        if not user:
            return Response(
                {"detail": "Identifiants invalides"},
                status=status.HTTP_401_UNAUTHORIZED
            )

        token, created = Token.objects.get_or_create(user=user)

        return Response({"token": token.key})