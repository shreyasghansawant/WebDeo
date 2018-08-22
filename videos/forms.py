from django import forms
from .models import Video, Comment, Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignUpForm (UserCreationForm):
    email = forms.EmailField (help_text="Please, Enter a Valid Email")
    first_name = forms.CharField (max_length=15, help_text="max length = 15characters")
    last_name = forms.CharField (max_length=15, help_text="max length = 15characters")

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class VideoForm (forms.ModelForm):
    class Meta:
        model = Video
        fields = ('title', 'video', 'description', 'thumbnail')


class ProfileForm (forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_picture', 'date_of_birth', 'bio')


class CommentForm (forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)


class EditUserForm (forms.ModelForm):
    email = forms.EmailField (help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only. ")
    first_name = forms.CharField (max_length=15)
    last_name = forms.CharField (max_length=15)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
