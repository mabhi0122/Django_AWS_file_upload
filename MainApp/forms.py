from django import forms
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .validators import validate_file_extensions, validate_file_size



class UserRegisterForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class UserLoginForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ['username', 'password']


class ProfileForm(forms.ModelForm):
    profile = forms.ImageField(
        validators=[validate_file_extensions, validate_file_size]
    )
    resume = forms.FileField(
        validators=[validate_file_extensions, validate_file_size],
        widget=forms.ClearableFileInput()
    )

    class Meta:
        model = Profile
        fields = ['name', 'profile', 'resume']
