from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User

from .serializers import RegisterSerializer
from drf_yasg.utils import swagger_auto_schema


class registerapi(APIView):
    @swagger_auto_schema(
        request_body=RegisterSerializer,
        responses={201: "User registered successfully", 400: "Bad request"},
    )
    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        user = User.objects.create(username=username, password=password)
        token = Token.objects.create(user=user)
        return Response({"token": token.key}, status=201)
