from .serializer import VideoSerializer, ProfileSerializer, LikeSerializer, CommentSerializer, UserSerializer
from django.contrib.auth.models import User
from videos.models import Video, Profile, Like, Comment

from rest_framework import generics
from rest_framework.permissions import IsAdminUser


# USER

class UserAPI (generics.ListCreateAPIView):
    queryset = User.objects.all ()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)


class UserAPIDetail (generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all ()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)


# VIDEO

class VideoAPI (generics.ListCreateAPIView):
    queryset = Video.objects.all ()
    serializer_class = VideoSerializer
    permission_classes = (IsAdminUser,)


class VideoAPIDetail (generics.RetrieveUpdateDestroyAPIView):
    queryset = Video.objects.all ()
    serializer_class = VideoSerializer
    permission_classes = (IsAdminUser,)


# PROFILE

class ProfileAPI (generics.ListCreateAPIView):
    queryset = Profile.objects.all ()
    serializer_class = ProfileSerializer
    permission_classes = (IsAdminUser,)


class ProfileAPIDetail (generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all ()
    serializer_class = ProfileSerializer
    permission_classes = (IsAdminUser,)


# LIKE

class LikeAPI (generics.ListCreateAPIView):
    queryset = Like.objects.all ()
    serializer_class = LikeSerializer
    permission_classes = (IsAdminUser,)


class LikeAPIDetail (generics.RetrieveUpdateDestroyAPIView):
    queryset = Like.objects.all ()
    serializer_class = LikeSerializer
    permission_classes = (IsAdminUser,)


# COMMENT

class CommentAPI (generics.ListCreateAPIView):
    queryset = Comment.objects.all ()
    serializer_class = CommentSerializer
    permission_classes = (IsAdminUser,)


class CommentAPIDetail (generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all ()
    serializer_class = CommentSerializer
    permission_classes = (IsAdminUser,)
