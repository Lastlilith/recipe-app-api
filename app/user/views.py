"""
Views for the user API
"""
from rest_framework import generics # type: ignore

from user.serializers import UserSerializer

class CreateUserView(generics.CreateAPIView):
    """Create user in a system"""
    serializer_class = UserSerializer

