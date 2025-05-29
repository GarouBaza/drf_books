from django.shortcuts import render
from .serializers import UserPublicSerializer, BookSerializer, ReviewSerializer

# Create your views here.

from rest_framework import viewsets, permissions
from .serializers import *
from .models import *

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

class CustomViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserPublicSerializer
    # permission_classes = [permissions.IsAuthenticated]

class RewiewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    # permission_classes = [permissions.IsAuthenticated]