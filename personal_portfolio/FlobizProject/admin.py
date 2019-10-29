from django.contrib import admin

from FlobizProject.models import Posts, Users, Comments

class PostsAdmin(admin.ModelAdmin):
    pass

class UsersAdmin(admin.ModelAdmin):
    pass


class CommentsAdmin(admin.ModelAdmin):
    pass

admin.site.register(Posts, PostsAdmin)
admin.site.register(Users, UsersAdmin)
admin.site.register(Comments, CommentsAdmin)