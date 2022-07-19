from rest_framework import serializers
from .models import BotUsers


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = BotUsers
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']

