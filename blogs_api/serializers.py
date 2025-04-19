from rest_framework import serializers
from django.contrib.auth.models import User

from blogs_api.models import Blog


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["username", "password"]

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = User.objects.filter(username=data["username"]).first()
        if not user:
            raise serializers.ValidationError("User not found")
        return data


class LogoutSerializer(serializers.Serializer):
    pass


class BlogSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")
    likes_count = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = ["id", "title", "content", "author", "created_at", "likes_count"]

    def get_likes_count(self, obj):
        return obj.likes.count()
