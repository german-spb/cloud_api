from rest_framework import serializers
from backend_api.models import User, UploadFiles

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class UploudFilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadFiles
        fields = '__all__'        
        