# base/urls.py
from django.urls import path
from .views import ( 
    StudentListCreateAPIView, 
    StudentRetrieveUpdateDestroyAPIView, 
    StudentByEmailApi, 
    StudentsByEnrollmentDateApi, 
    TotalStudentsApi
)


urlpatterns = [
    # path('', home, name='home'),
    path('students/', StudentListCreateAPIView.as_view(), name='student-list-create'),
    path('students/<int:pk>/', StudentRetrieveUpdateDestroyAPIView.as_view(), name='student-detail'),  
    path('students/email/<str:email>/', StudentByEmailApi.as_view(), name='student-by-email'),
    path('students/enrollment/<str:date>/', StudentsByEnrollmentDateApi.as_view(), name='students-by-enrollment-date'),
    path('students/total/', TotalStudentsApi.as_view(), name='total-students'),
    
]
