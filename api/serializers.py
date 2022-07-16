from rest_framework import serializers
from .models import BotUsers


class UsersListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BotUsers
        fields = ['user_id', 'first_name', 'last_name', 'username']
