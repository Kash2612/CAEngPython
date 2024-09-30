# base/urls.py
from django.urls import path
from .views import StudentListCreateAPIView, StudentRetrieveUpdateDestroyAPIView


urlpatterns = [
    # path('', home, name='home'),
    path('students/', StudentListCreateAPIView.as_view(), name='student-list-create'),
    path('students/<int:pk>/', StudentRetrieveUpdateDestroyAPIView.as_view(), name='student-detail'),  
]
