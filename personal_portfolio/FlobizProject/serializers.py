from rest_framework import serializers
from FlobizProject.models import Posts, Users, Comments
from rest_framework.serializers import (
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField
    )

class CommentSerializer(ModelSerializer):
    reply_count = SerializerMethodField()
    class Meta:
        model = Users
        fields = [
            'first_name',
            'email',
            'gender',
            'age',
            'post_count',
            'comment_count',
        ]
    
    def get_post_count(self, obj):
        if obj.is_parent:
            return obj.posts.count()
        return 0

    def get_comment_count(self, obj):
        if obj.is_parent:
            return obj.comments.count()
        return 0