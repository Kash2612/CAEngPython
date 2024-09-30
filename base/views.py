  # views.py
from rest_framework import generics
from .models import Student
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from .serializers import StudentSerializer
from django.http import HttpResponse
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny, IsAuthenticated


def home(request):
    return HttpResponse("Welcome to the Student API!")


class StudentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]


class StudentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class CustomAuthToken(ObtainAuthToken):
    """ Custom Token Authentication View """
    def post(self, request, *args, **kwargs):
        # Call the base class method to authenticate user and get token
        response = super().post(request, *args, **kwargs)
        # Extract the user from the request data
        username = request.data.get('username')
        try:
            user = User.objects.get(username=username)  # Get user from the username
            token, created = Token.objects.get_or_create(user=user)  # Get or create token
            return Response({'token': token.key})  # Return the token in the response
        except User.DoesNotExist:
            return Response({"error": "User does not exist."}, status=400)  # Handle user not found
