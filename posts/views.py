from .serializers import PostSerializer, UserSerializer
from django.contrib.auth import get_user_model
from .models import Post
from .permissions import IsAuthorOrReadOnly
from rest_framework.viewsets import ModelViewSet

# Create your views here.

# class PostListAPIView(ListCreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#
#
# class PostDetailAPIView(RetrieveUpdateDestroyAPIView):
#     permission_classes = [IsAuthorOrReadOnly]
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#
#
# class UserListAPIView(ListCreateAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer
#
#
# class UserDetailAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer


class PostViewSet(ModelViewSet):
    permission_classes = [IsAuthorOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

