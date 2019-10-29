"""personal_portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url, include
from FlobizProject import views



from FlobizProject.resources import PostResource, UsersResource, CommentsResource
post_resource = PostResource()
users_resource = UsersResource()
comments_resource = CommentsResource()

urlpatterns = [
    path('admin/', admin.site.urls),
	path("posts/", include("FlobizProject.urls")),
	path("post_detail/<int:pk>/", views.post_detail, name="post_detail"),
	path('edit_post/<int:pk>/',views.post_Edit,name="post_Edit"),
    url(r'^FlobizProject/', include(post_resource.urls)),
	url(r'^FlobizProject/', include(users_resource.urls)),
	url(r'^FlobizProject/', include(comments_resource.urls)),
	#url(r'^FlobizProject/', include(postcounts_resource.urls)),
    url(r'^FlobizProject/',views.posts_index,name='index'),

	url(r'^edit_profile/$',views.editProfile,name='user_profile'),
	url(r'^logout_user/$',views.logout_user,name='logout_user'),
	

	#path('', include('hello_world.urls')),
]
