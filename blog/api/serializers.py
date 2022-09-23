from rest_framework import serializers
from blog.models import Post


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        exclude = ('modified_at', 'published_at',)