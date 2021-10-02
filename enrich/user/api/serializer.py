from rest_framework import serializers
from django.contrib.auth.models import Group
from ..models import NewUser,LanguageConvert

class GroupSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Group
        fields ='__all__'


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = NewUser
        fields ='__all__'

class LanguageConverterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = LanguageConvert
        fields ='__all__'