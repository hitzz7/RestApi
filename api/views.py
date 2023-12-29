from rest_framework import viewsets
from .serializers import ApiSerializer,CommentSerializer,AlbumSerializer,PhotoSerializer,TodosSerializer,UserSerializer
import requests
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

class ApiViewSet(viewsets.ViewSet):
    serializer_class = ApiSerializer
    # permission_classes = [permissions.AllowAny]
    
    

    def get_queryset(self):
        # Fetch data from JSONPlaceholder
        response = requests.get('https://jsonplaceholder.typicode.com/posts')
        data = response.json()
        return data
    
    def list(self, request):
        response = requests.get('https://jsonplaceholder.typicode.com/posts')
        posts = response.json()
        serializer = ApiSerializer(posts, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{pk}')
        return Response(response.json())


    def create(self, request):
        serializer = ApiSerializer(data=request.data)
        if serializer.is_valid():
            # Perform the actual creation using the external API
            response = requests.post('https://jsonplaceholder.typicode.com/posts', json=serializer.validated_data)
            return Response(response.json(), status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        # Fetch the current data from the external API
        current_data = self.get_queryset()
        
        # Find the object to update based on the provided 'pk'
        instance_to_update = next((item for item in current_data if item['id'] == int(pk)), None)

        if instance_to_update:
            serializer = ApiSerializer(instance_to_update, data=request.data, partial=True)
            if serializer.is_valid():
                # Perform the actual update using the external API
                response = requests.put(f'https://jsonplaceholder.typicode.com/posts/{pk}', json=serializer.validated_data)
                return Response(response.json())
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'detail': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        # Fetch the current data from the external API
        current_data = self.get_queryset()

        # Find the object to delete based on the provided 'pk'
        instance_to_delete = next((item for item in current_data if item['id'] == int(pk)), None)

        if instance_to_delete:
            # Perform the actual deletion using the external API
            response = requests.delete(f'https://jsonplaceholder.typicode.com/posts/{pk}')
            return Response({'status': 'successfully deleted'}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'status': 'no such ID'}, status=status.HTTP_404_NOT_FOUND)
    
    
        
    
class CommentViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')

        if post_id:
            # Fetch comments for a specific post
            response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{post_id}/comments')
        else:
            # Fetch all comments
            response = requests.get('https://jsonplaceholder.typicode.com/comments')

        return response.json()
    
    
    
    
class AlbumViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = AlbumSerializer

    def get_queryset(self):
        # Fetch data from JSONPlaceholder
        user_id = self.kwargs.get('user_id')
        
        if user_id:
            response = requests.get(f'https://jsonplaceholder.typicode.com/user/{user_id}/albums')
        else:
            response = requests.get('https://jsonplaceholder.typicode.com/albums')
            
        return response.json()
    
class PhotoViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PhotoSerializer

    def get_queryset(self):
        # Fetch data from JSONPlaceholder
        album_id = self.kwargs.get('album_id')
        
        if album_id:
            response = requests.get(f'https://jsonplaceholder.typicode.com/albums/{album_id}/photos')
        else:
            response = requests.get('https://jsonplaceholder.typicode.com/photos')
            
        return response.json()
    
class TodosViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = TodosSerializer

    def get_queryset(self):
        # Fetch data from JSONPlaceholder
        user_id = self.kwargs.get('user_id')
        
        if user_id:
            response = requests.get(f'https://jsonplaceholder.typicode.com/user/{user_id}/todos')
        else:
            response = requests.get('https://jsonplaceholder.typicode.com/todos')
            
        return response.json()
    
    
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        # Fetch data from JSONPlaceholder
        response = requests.get('https://jsonplaceholder.typicode.com/users')
        data = response.json()
        return data