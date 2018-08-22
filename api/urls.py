from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

app_name = "api"

urlpatterns = [
    path ('user/', views.UserAPI.as_view(), name="user"),
    path ('user/<int:pk>/', views.UserAPIDetail.as_view(), name="user-detail"),
    path ('video/', views.VideoAPI.as_view(), name="video"),
    path ('video/<int:pk>/', views.VideoAPIDetail.as_view(), name="video-detail"),
    path ('profile/', views.ProfileAPI.as_view(), name="profile"),
    path ('profile/<int:pk>/', views.ProfileAPIDetail.as_view(), name="profile-detail"),
    path ('like/', views.LikeAPI.as_view(), name="like"),
    path ('like/<int:pk>/', views.LikeAPIDetail.as_view(), name="like-detail"),
    path ('comment/', views.CommentAPI.as_view(), name="comment"),
    path ('comment/<int:pk>/', views.CommentAPIDetail.as_view(), name="comment-detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
