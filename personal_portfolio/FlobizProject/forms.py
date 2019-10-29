from django import forms
from FlobizProject.models import Users, Posts
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = Users
        fields = ('first_name','last_name','email', 'password', 'bio','gender','age')


class UserProfileForm(forms.ModelForm):
    #password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = Users
        fields = ('first_name','last_name', 'bio','gender','age')

class PostForm(forms.ModelForm):
    
    class Meta():
        model = Posts
        fields = ('id','title','description','likes', 'image_url')


class PostDetailForm(forms.ModelForm):
    
    class Meta():
        model = Posts
        fields = ('id','title','description','likes', 'image_url')
