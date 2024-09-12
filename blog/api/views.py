from rest_framework import generics, viewsets

from blog.api.serializers import PostSerializer, UserSerializer, PostDetailSerializer
from blog.models import Post
from blog.api.permissions import AuthorModifyOrReadOnly, IsAdminUserForObject
from blango_auth.models import User
from blog.api.serializers import PostSerializer, UserSerializer
from blog.api.filters import PostFilterSet

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    permission_classes = [AuthorModifyOrReadOnly | IsAdminUserForObject]


class UserDetail(generics.RetrieveAPIView):
    lookup_field = "email"
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filterset_class = PostFilterSet
    # filterset_fields can be removed
    # other existing attributes and methods omitted