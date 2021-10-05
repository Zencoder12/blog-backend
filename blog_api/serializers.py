from rest_framework import serializers
from blog.models import Post
from django.conf import settings


class PostSerializer(serializers.ModelSerializer):
    # overriding title and content in order to use the min_lenght validation from rest_framework
    author = serializers.StringRelatedField()
    category = serializers.StringRelatedField()
    content = serializers.CharField(max_length=1024, min_length=10)
    title = serializers.CharField(
        max_length=250, min_length=3)

    class Meta:
        model = Post
        fields = ('category', 'id', 'title', 'slug', 'author',
                  'excerpt', 'content', 'status', 'published')


class UserRegisterSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(required=True)
    username = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = settings.AUTH_USER_MODEL
        fields = ('email', 'user_name', 'first_name')
        extra_kwargs = {'password': {'write_only': True}}
