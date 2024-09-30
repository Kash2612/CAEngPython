# base/urls.py
from django.urls import path
from .views import StudentListCreateAPIView, StudentRetrieveUpdateDestroyAPIView
from base.views import home, CustomAuthToken

urlpatterns = [
    path('', home, name='home'),
    path('students/', StudentListCreateAPIView.as_view(), name='student-list-create'),
    path('students/<int:pk>/', StudentRetrieveUpdateDestroyAPIView.as_view(), name='student-detail'),
    path('token-auth/', CustomAuthToken.as_view(), name='token_auth'),  # Ensure this is correctly pointing to your view
]
