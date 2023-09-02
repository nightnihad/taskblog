from django import forms
from .models import Article, Comments
from django.contrib.auth.models import User
from django.contrib.auth.forms import  UserCreationForm
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title','subject','category']
        
class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['subject']
        
# class RegisterForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['first_name','password']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(required=True,widget=forms.PasswordInput(attrs={'class':'fields'}))