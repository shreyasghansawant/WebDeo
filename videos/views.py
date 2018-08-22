from django.shortcuts import render, redirect
from .forms import SignUpForm, VideoForm, ProfileForm, CommentForm, EditUserForm
from .models import Video, Like, Comment, Profile
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash


# VIDEOS

def index(request):
    videos = Video.objects.all ().order_by ('-date', '-time')
    return render (request, 'videos/index.html', {'videos': videos})


def detail(request, video_id):
    video = Video.objects.get (pk=video_id)
    form = CommentForm ()
    num_comments = Comment.objects.filter (video=video).count ()
    comments = Comment.objects.filter (video=video).order_by ('-date_time')
    try:
        liked = Like.objects.get (user=request.user, video=video)
        if liked:
            video_liked = "Done"
    except Exception:
        video_liked = None
    likes = Like.objects.filter (video=video).count ()
    video.views += 1
    video.save ()
    return render (request, 'videos/detail.html', {
        'video': video,
        'likes': likes,
        'video_liked': video_liked,
        'form': form,
        'num_comments': num_comments,
        'comments': comments,
    })


@login_required (login_url='videos:login')
def addVideoView(request):
    if request.method == "POST":
        form = VideoForm (request.POST, request.FILES)

        if form.is_valid ():
            instance = form.save (commit=False)
            instance.admin = request.user
            instance.save ()
            return redirect ('videos:detail', instance.id)

    else:
        form = VideoForm ()

    return render (request, 'videos/add-video.html', {'form': form})


@login_required (login_url='videos:login')
def deleteVideo(request, video_id):
    if request.method == "POST":
        video = Video.objects.get (pk=video_id)
        if request.user == video.admin:
            video.delete ()
        return redirect ('videos:my-profile')


@login_required (login_url='videos:login')
def updateVideo(request, video_id):
    video = Video.objects.get (pk=video_id)
    if request.method == "POST":
        if request.user == video.admin:
            form = VideoForm (request.POST or None, request.FILES or None, instance=video)

            if form.is_valid ():
                form.save ()
                return redirect ('videos:detail', video.id)

    else:
        form = VideoForm (instance=video)

    return render (request, 'videos/add-video.html', {
        'form': form,
        'update': 'update this'
    })


# ACCOUNTS

def signUpView(request):
    if request.method == "POST":
        form = SignUpForm (request.POST)

        if form.is_valid ():
            user = form.save ()
            user_profile = Profile.objects.create (user=user)
            user_profile.save ()
            login (request, user)

            # Email
            subject = "Thanks for Creating New Videos Account"
            text = "Hello " + user.username + ", \n" \
                                              "    Welcome to Videos Web App.\n" \
                                              "You can do many things in this web app,\n" \
                                              "So go and explore the web app\n" \
                                              "and if you have any problem\n" \
                                              "please contact me on this email.\n" \
                                              "shreyasghansawant@gmail.com\n\n" \
                                              "Thank You"
            admin = settings.EMAIL_HOST_USER
            send_mail (subject, text, admin, [user.email], fail_silently=True)

            return redirect ('videos:edit-profile')

    else:
        form = SignUpForm ()

    return render (request, 'videos/signup.html', {'form': form})


def logInView(request):
    if request.method == "POST":
        form = AuthenticationForm (data=request.POST)

        if form.is_valid ():
            user = form.get_user ()
            login (request, user)
            return redirect ('videos:index')

    else:
        form = AuthenticationForm ()

    return render (request, 'videos/login.html', {'form': form})


@login_required (login_url='videos:login')
def logOutView(request):
    if request.method == "POST":
        logout (request)
        return redirect ('videos:index')


@login_required (login_url='videos:login')
def password_change_view(request):
    if request.method == "POST":
        form = PasswordChangeForm (request.user, request.POST)

        if form.is_valid ():
            user = form.save ()
            update_session_auth_hash (request, user)
            return redirect ('videos:my-profile')

    else:
        form = PasswordChangeForm (request.user)

    return render (request, 'videos/edit-password.html', {'form': form})


@login_required (login_url='videos:login')
def delete_user(request):
    if request.method == "POST":
        if request.user:
            request.user.delete ()
            return redirect ('videos:index')


# PROFILE

@login_required (login_url='videos:login')
def myProfile(request):
    user = request.user
    videos = Video.objects.filter (admin=user).order_by ('-date', '-time')
    return render (request, 'videos/my-profile.html', {
        'videos': videos,
        'user': user,
    })


def profile(request, video_id):
    video = Video.objects.get (pk=video_id)
    user = video.admin

    if user == request.user:
        return redirect ('videos:my-profile')

    videos = Video.objects.filter (admin=user).order_by ('-date', '-time')
    return render (request, 'videos/profile.html', {
        'videos': videos,
        'user_p': user,
    })


@login_required (login_url='videos:login')
def profileEditView(request):
    user_profile = Profile.objects.get (user=request.user)

    if user_profile.user == request.user:

        if request.method == "POST":
            form = ProfileForm (request.POST or None, request.FILES or None, instance=user_profile)
            form_u = EditUserForm (request.POST or None, instance=request.user)

            if form.is_valid () and form_u.is_valid ():
                form.save ()
                user = form_u.save ()
                update_session_auth_hash (request, user)
                return redirect ('videos:my-profile')

        else:
            form = ProfileForm (instance=user_profile)
            form_u = EditUserForm (instance=request.user)

        return render (request, 'videos/edit-profile.html', {
            'form': form,
            'form_u': form_u,
        })


def comment_profile(request, comment_user):
    user = User.objects.get (pk=comment_user)
    if user == request.user:
        return redirect ('videos:my-profile')

    videos = Video.objects.filter (admin=user).order_by ('-date', '-time')
    return render (request, 'videos/profile.html', {
        'videos': videos,
        'user': user,
    })


# LIKE

@login_required (login_url='videos:login')
def like(request, video_id):
    if request.method == "POST":
        video = Video.objects.get (pk=video_id)
        video.views -= 1
        video.save ()
        try:
            liked = Like.objects.get (user=request.user, video=video)
            if liked:
                return redirect ('videos:detail', video.id)
        except Exception:
            like = Like.objects.create (user=request.user, video=video)
            like.save ()
            return redirect ('videos:detail', video.id)


@login_required (login_url='videos:login')
def unlike(request, video_id):
    if request.method == "POST":
        video = Video.objects.get (pk=video_id)
        video.views -= 1
        video.save ()
        try:
            liked = Like.objects.get (user=request.user, video=video)
            if liked:
                if liked.user == request.user:
                    liked.delete ()
                    return redirect ('videos:detail', video.id)
        except Exception:
            return redirect ('videos:detail', video.id)


@login_required (login_url='videos:login')
def liked_videos(request):
    likes = Like.objects.filter (user=request.user)
    return render (request, 'videos/like.html', {'likes': likes})


# COMMENT

@login_required (login_url='videos:login')
def comment(request, video_id):
    video = Video.objects.get (pk=video_id)
    if request.method == "GET":
        comment_text = request.GET.get ('c_text', None)
        user_comment = Comment.objects.create (user=request.user, video=video, text=comment_text)
        user_comment.save ()
        video.views -= 1
        video.save ()
        return redirect ('videos:detail', video.id)


@login_required (login_url='videos:login')
def delete_comment(request, comment_id):
    user_comment = Comment.objects.get (pk=comment_id)
    video = user_comment.video
    video.views -= 1
    video.save ()
    if user_comment.user == request.user:
        user_comment.delete ()
        return redirect ('videos:detail', video.id)
    return redirect ('videos:detail', video.id)


# SEARCH | ABOUT

def search(request):
    if request.method == "GET":
        searched_text = request.GET.get ('s_text', None)
        videos = Video.objects.filter (title__contains=searched_text).order_by ('-date', '-time')
        return render (request, 'videos/index.html', {
            'videos': videos,
            'searched_text': searched_text,
        })


def about(request):
    return render (request, 'videos/about.html', {})
