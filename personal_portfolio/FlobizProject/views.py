from django.shortcuts import render
from FlobizProject.models import Posts, Users
from rest_framework.decorators  import api_view
from rest_framework.response import Response
from rest_framework import status
from FlobizProject.serializers import CommentSerializer
from FlobizProject.forms import UserForm, PostForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django.contrib.auth import logout

def posts_index(request):
    posts = Posts.objects.filter(author_id=request.user.id)
    print(posts)
    context = {
        'posts': posts
    }
    return render(request, 'posts_index.html', context)
	
	
def post_detail(request, pk):
    postd = Posts.objects.get(pk=pk)
    context = {
        'postd': postd
    }
    return render(request, 'post_detail.html', context)



@api_view(['GET'])
def post_comment_count(request):
    response_data = {"data": []}
    if request and request.id:
        response_data["data"] = CommentSerializer(
                                    context={"id": request.id},
                                    many=True
                                ).data
    return Response(response_data, status=status.HTTP_200_OK)
	
	
	
def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        #profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.username = user.email
            user.save()
            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()
        
    return render(request,'registration.html',
                          {'user_form':user_form,
                           'registered':registered})

def editProfile(request):
    edited = False
    user = request.user
    userd = Users.objects.get(id=user.id)
    if request.method == 'POST':
        user_form = UserProfileForm(data=request.POST)
        #profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            #user.set_password(user.password)
            userd.first_name = user.first_name
            userd.last_name = user.last_name
            userd.age = user.age
            userd.bio = user.bio
            userd.gender= user.gender
            userd.save()
            edited = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserProfileForm(initial={'first_name': userd.first_name, 'last_name': userd.last_name, 'bio':userd.bio, 'gender': userd.gender, 'age': userd.age})
        
    return render(request,'registration.html',
                          {'user_form':user_form,
                           'registered':edited})

						   
def index(request):
    return render(request,'index.html')
	
	
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'login.html', {})
        

def addNewPost(request):
    added = False
    if request.method == 'POST':
        post_form = PostForm(data=request.POST)
        #profile_form = UserProfileInfoForm(data=request.POST)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            user = request.user
            post.author = user
            post.save()
            added = True
        else:
            print(post_form.errors)
    else:
        post_form = PostForm()
        
    return render(request,'AddNewPost.html',
                          {'post_form':post_form,
                           'added':added})
		

def post_Edit(request, pk):
    print('hello')
    edited = False
    if request.method == 'POST':
        post_form = PostForm(data=request.POST)
        #profile_form = UserProfileInfoForm(data=request.POST)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            user = request.user
            dpost = Posts.objects.get(id=pk)
            dpost.title = post.title
            dpost.description = post.description
            dpost.likes = post.likes
            dpost.image_url = post.image_url
            print('pk value ', pk)
            dpost.id = pk
            #post.author = user
            dpost.save()
            edited = True
            return posts_index(request)
        else:
            print(post_form.errors)
            return render(request, 'AddNewPost.html', {'post_form':post_form,
                           'added': False,'edited':edited})

    else:
        postd = Posts.objects.get(pk=pk)
        post_form = PostForm(initial={'title': postd.title, 'description': postd.description, 'likes':postd.likes, 'image_url': postd.image_url})
        context = {
            'postd': postd
        }
        return render(request, 'AddNewPost.html', {'post_form':post_form,
                           'added': False,'edited':edited})

def logout_user(request):
    logout(request)
    return user_login(request);