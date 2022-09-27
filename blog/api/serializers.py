from rest_framework import serializers
from blog.models import Post, Tag, Comment, User
from versatileimagefield.serializers import VersatileImageFieldSerializer


class TagField(serializers.SlugRelatedField):
    def to_internal_value(self, data):
        try:
            return self.get_queryset().get_or_create(value=data.lower())[0]
        except (TypeError, ValueError):
            self.fail(f"Tag value {data} is invalid")


class PostSerializer(serializers.ModelSerializer):
    tags = TagField(
        slug_field="value", many=True,
        queryset=Tag.objects.all()
    )
    hero_image = VersatileImageFieldSerializer(
        sizes=[
            ("full_size", "url"),
            ("thumbnail", "thumbnail__100x100"),
        ],
        read_only=True,
    )

    class Meta:
        model = Post
        exclude = ["ppoi"]


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]


class CommentSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    creator = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ["id", "creator", "content", "modified_at", "created_at"]
        readonly = ["modified_at", "created_at"]


class PostDetailSerializer(PostSerializer):
    comments = CommentSerializer(many=True)
    hero_image = VersatileImageFieldSerializer(
        sizes=[
            ("full_size", "url"),
            ("thumbnail", "thumbnail__100x100"),
            ("square_crop", "crop__200x200"),
        ],
        read_only=True,
    )
    # {
    #     "id": 6,
    #     "hero_image": {
    #         "square_crop": "http://127.0.0.1:8000/media/__sized__/hero_images/snake-419043_1920-crop-c0-74__0-52-200x200-70.jpg",
    #         "full_size": "http://127.0.0.1:8000/media/hero_images/snake-419043_1920.jpg",
    #         "thumbnail": "http://127.0.0.1:8000/media/__sized__/hero_images/snake-419043_1920-thumbnail-100x100-70.jpg"
    #     },
    #     ...
    # }

    def update(self, instance, validated_data):
        comments = validated_data.pop("comments")
        instance = super(PostDetailSerializer, self).update(instance, validated_data)
        for comment_data in comments:
            if comment_data.get("id"):
            # comment has an ID so was pre-existing
                continue
            comment = Comment(**comment_data)
            comment.creator = self.context["request"].user
            comment.content_object = instance
            comment.save()
        return instance
