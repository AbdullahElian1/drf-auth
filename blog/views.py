from rest_framework import permissions
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Blog
from .serializers import BLogSerializer
from .permissions import IsOwnerOrReadOnly


class BlogsList(ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BLogSerializer



class BlogsDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Blog.objects.all()
    serializer_class = BLogSerializer

