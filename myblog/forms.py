from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Comments
class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields=['username','email','password1','password2']
        

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        exclude=['post','user']