from django.db import models
from django.contrib.auth.models import AbstractUser

class Users(AbstractUser):
	email = models.CharField(max_length=50)
	password = models.CharField(max_length=200)
	bio = models.TextField()
	gender = models.CharField(max_length=10)
	age = models.IntegerField()    
	first_name = models.CharField(max_length=200)    
	last_name = models.CharField(max_length=200)
	created_on = models.DateTimeField(auto_now_add=True)
	last_modified = models.DateTimeField(auto_now=True)
	
	USERNAME_FIELD = "email"
	REQUIRED_FIELDS = ['password']

	    
	    

	    
    
class Posts(models.Model):
	title=models.CharField(max_length=200)    
	description=models.TextField()    
	likes=models.IntegerField()    
	image_url=models.CharField(max_length=200)       
	author = models.ForeignKey(Users, on_delete=models.CASCADE, blank= True) 
	created_on = models.DateTimeField(auto_now_add=True)
	last_modified = models.DateTimeField(auto_now=True)    
	    
	    
class Comments(models.Model):
	commented_by=models.CharField(max_length=200)    
	post_id=models.ForeignKey(Posts, on_delete=models.CASCADE, blank= True)    
	comments=models.CharField(max_length=200)
	created_on = models.DateTimeField(auto_now_add=True)
	last_modified = models.DateTimeField(auto_now=True)    
	    
    
