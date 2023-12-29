from rest_framework import serializers

class ApiSerializer(serializers.Serializer):
    # Define your serializer fields here
    userId = serializers.IntegerField()
    
    title = serializers.CharField(max_length=255)
    body = serializers.CharField()
    
    
    
    
    
    
class CommentSerializer(serializers.Serializer):
    postId=serializers.IntegerField()
    id=serializers.IntegerField()
    name = serializers.CharField()
    email = serializers.EmailField()
    body = serializers.CharField()
    
class AlbumSerializer(serializers.Serializer):
    userId = serializers.IntegerField()
    id=serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    
class PhotoSerializer(serializers.Serializer):
    albumId=serializers.IntegerField()
    id=serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    url = serializers.URLField()
    thumbnailUrl = serializers.URLField()

class TodosSerializer(serializers.Serializer):
    userId = serializers.IntegerField()
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    completed = serializers.BooleanField()
    
class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=255)
    username = serializers.CharField(max_length=255)
    email = serializers.EmailField()
    address = serializers.DictField()
    phone = serializers.CharField(max_length=20)
    website = serializers.URLField()
    company = serializers.DictField()


    
    
