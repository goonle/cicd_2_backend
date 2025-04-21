from rest_framework import serializers
from django.contrib.auth.models import User

from blogs_api.models import Blog, Like


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
    liked = serializers.SerializerMethodField()
    is_author = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = ["id", "title", "content", "author", "created_at", "likes_count", "liked", "is_author"]

    def get_likes_count(self, obj):
        return obj.likes.count()

    def get_liked(self, obj):
        user = self.context["request"].user
        if user.is_authenticated:
            return Like.objects.filter(user=user, blog=obj).exists()
        return False

    def get_is_author(self, obj):
        user = self.context["request"].user
        return user.is_authenticated and obj.author == user
