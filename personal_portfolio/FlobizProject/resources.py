from tastypie.resources import ModelResource
from FlobizProject.models import Posts, Users, Comments
from tastypie.authorization import Authorization
from rest_framework import serializers

class PostResource(ModelResource):
    class Meta:
        queryset = Posts.objects.all()
        resource_name = 'post'
        authorization = Authorization()
		
		
		
class UsersResource(ModelResource):
    class Meta:
        queryset = Users.objects.all()
        resource_name = 'users'
        authorization = Authorization()
		
		
class CommentsResource(ModelResource):
    class Meta:
        queryset = Comments.objects.all()
        resource_name = 'comments'
        authorization = Authorization()
		

