from videos.models import Video, Profile, Like, Comment
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User


class VideoSerializer (ModelSerializer):
    class Meta:
        model = Video
        fields = "__all__"


class ProfileSerializer (ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"


class LikeSerializer (ModelSerializer):
    class Meta:
        model = Like
        fields = "__all__"


class CommentSerializer (ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class UserSerializer (ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
