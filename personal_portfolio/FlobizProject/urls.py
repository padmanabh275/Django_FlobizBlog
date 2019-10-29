from django.urls import path
from django.conf.urls import url, include

from . import views

urlpatterns = [
    path("", views.posts_index, name="posts_index"),
    
	path('count/', views.post_comment_count),
    url(r'^register/$',views.register,name='register'),
	url(r'^user_login/$',views.user_login,name='user_login'),
	url(r'^new_post/$',views.addNewPost,name='new_post'),
	path('edit_post/<int:pk>/',views.post_Edit,name="post_Edit"),
	url(r'^edit_profile/$',views.editProfile,name='user_profile'),




]