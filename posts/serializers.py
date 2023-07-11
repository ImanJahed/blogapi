from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Posts


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "author",
            "title",
            "content",
            "created_date",
        )
        model = Posts


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'username']