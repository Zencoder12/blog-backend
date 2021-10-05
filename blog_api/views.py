from rest_framework import generics, filters
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny
from blog.models import Post
from .serializers import PostSerializer
from .custom_permissions import PostUserWritePermission
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect, csrf_exempt


class PostList(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetailBySlug(generics.RetrieveAPIView):
    queryset = Post.published_objects.all()
    serializer_class = PostSerializer

    def get_object(self):
        item = self.kwargs.get('pk')
        return get_object_or_404(Post, slug=item)


class PostSearch(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['^slug']


# Post Admin

class CreatePost(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class EditPost(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated & PostUserWritePermission]
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class DeletePost(generics.RetrieveDestroyAPIView):
    permission_classes = [IsAuthenticated & PostUserWritePermission]
    queryset = Post.objects.all()
    serializer_class = PostSerializer


# class GetCSRFToken(APIView):
#     permission_classes = [AllowAny]

#     @method_decorator(ensure_csrf_cookie)
#     def dispatch(self, *args, **kwargs):
#         return super().dispatch(*args, **kwargs)

#     def get(self, request, format=None):
#         return Response({'success': 'CSRF cookie set'})
