from rest_framework import serializers
from .models import CustomUser,Student, LibraryHistory, FeesHistory

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'role']

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class LibraryHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = LibraryHistory
        fields = '__all__'

class FeesHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FeesHistory
        fields = '__all__'
