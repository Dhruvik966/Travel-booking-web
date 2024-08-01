from rest_framework import serializers 
from mytraveladmin import models
from django.contrib.auth.models import User

class PackagesSerialize(serializers.ModelSerializer):
    class Meta:
        model = models.Packages
        fields = '__all__'
        

class CategoriesSerialize(serializers.ModelSerializer):
    class Meta:
        model = models.Categories
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user