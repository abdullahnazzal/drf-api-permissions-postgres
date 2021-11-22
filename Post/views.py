from django.shortcuts import render
from rest_framework import generics, serializers
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializer import PostSerializer
from .models import Post
from .permissions import IsAuthorOrReadOnly
# Create your views here.
class PostList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class =PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class =PostSerializer
