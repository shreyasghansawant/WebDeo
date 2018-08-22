from django.urls import path
from . import views

app_name = "videos"

urlpatterns = [

    path ('', views.index, name="index"),
    path ('video_id=<int:video_id>/', views.detail, name="detail"),
    path ('add/video/', views.addVideoView, name="add-video"),
    path ('delete/video_id=<int:video_id>/', views.deleteVideo, name="delete-video"),
    path ('update/video_id=<int:video_id>/', views.updateVideo, name="update-video"),

    path ('signup/', views.signUpView, name="signup"),
    path ('login/', views.logInView, name="login"),
    path ('logout/', views.logOutView, name="logout"),
    path ('edit/password/', views.password_change_view, name="edit-password"),
    path ('delete/user/', views.delete_user, name="delete-user"),

    path ('my-profile/', views.myProfile, name="my-profile"),
    path ('video_id=<int:video_id>/profile/', views.profile, name="profile"),
    path ('edit/profile/', views.profileEditView, name="edit-profile"),
    path ('profile/comment_user_id=<int:comment_user>/', views.comment_profile, name="comment-profile"),

    path ('like/video_id=<int:video_id>/', views.like, name="like"),
    path ('unlike/video_id=<int:video_id>/', views.unlike, name="unlike"),
    path ('liked/videos/', views.liked_videos, name="liked-videos"),

    path ('comment/video_id=<int:video_id>/', views.comment, name="comment"),
    path ('delete/comment/video_id=<int:comment_id>/', views.delete_comment, name="delete-comment"),

    path ('search/', views.search, name="search"),
    path ('about/', views.about, name="about"),
]
