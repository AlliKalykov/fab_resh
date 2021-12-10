from rest_framework import serializers
from  .models import UserProfile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'
        # fields = ('username', 'password', 'first_name', 'last_name', 'email', 'last_login', 'is_superuser', 'last_login',
        #           'is_staff', 'is_active', 'date_joined')
        # read_only_fields = ('last_login', 'is_superuser', 'last_login', 'is_staff', 'is_active', 'date_joined')
