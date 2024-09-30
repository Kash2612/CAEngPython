  # views.py\
from django.shortcuts import render
from rest_framework import generics, status
from .models import Student
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import StudentSerializer, LoginSerializer
from django.http import HttpResponse
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated


# def home(request):
#     return HttpResponse("Welcome to the Student API!")


class StudentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    # FOR DELETE BUTTON
    def delete(self, request, *args, **kwargs):
        Student.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class StudentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # lookup_field='pk'
        

class StudentApi(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        queryset= Student.objects.all()
        serializer= StudentSerializer(queryset, many=True)
        return Response({
            "status" : True,
            "data": serializer.data
        })

class LoginApi(APIView):
    def post(self, request):
        data=request.data 
        print(data)
        serializer=LoginSerializer(data=data)
        if not serializer.is_valid():
            return Response({
                "status" : False,
                "data": serializer.errors
        })  
        username= serializer.data['username']
        password= serializer.data['password']

        print(username,password)

        user_obj= authenticate(username=username, password=password)
        if user_obj:
            token, created=Token.objects.get_or_create(user=user_obj) 
            return Response({
                "status": True,
                "data": {"token": token.key}
            })

        return Response({
                "status" : True,
                "data": {},
                "message": "Invalid credentials"
        })

