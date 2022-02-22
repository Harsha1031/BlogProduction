from django import forms
from Blog.models import PosModel
from django.contrib.auth.models import User

from Blog import models


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta():
        model = User
        fields = ('username','password')

    
class PostForm(forms.ModelForm):
    
    title=forms.CharField()
    text=forms.CharField()

    class Meta():
        model = PosModel
        fields = ('title','text')


class CommentForm(forms.ModelForm):
    text=forms.Textarea()

    class Meta():
        model=models.CommentModel
        fields=('text',)