from django.shortcuts import render
from .models import User, UploadFiles
from .serializers import UserSerializer, UploudFilesSerializer
from rest_framework import viewsets

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class UploudFilesViewSet(viewsets.ModelViewSet):
    serializer_class = UploudFilesSerializer
    queryset = UploadFiles.objects.all()         