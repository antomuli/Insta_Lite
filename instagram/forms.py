from django import forms
from .models import Image, Profile, Comments
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=80, help_text='Required')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['likes', 'posted', 'profile', 'profile_det', 'comments']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        exclude = ['image', 'user']