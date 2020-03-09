from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from app.models import User
from app.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    允许用户查看或编辑的API路径。
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer