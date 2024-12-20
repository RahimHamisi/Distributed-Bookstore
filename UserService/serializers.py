from datetime import date
from rest_framework import serializers # type: ignore
from .models import User, UserProfile
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer # type: ignore


class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id', 'username', 'email','date_joined','password']

class UserProfileSerializer(serializers.ModelSerializer):
    age=serializers.SerializerMethodField(method_name="calculate_age")
    user=UserCreateSerializer
    

    class Meta:
        model = UserProfile
        fields = ['id', 'user', 'phone_number', 'address','birth_date','age']
       

        def calculate_age(self,obj):
            if obj.birth_date is not None:
                today = date.today()
                age=today.year-obj.birth_date.year
                return age
            return None 
                