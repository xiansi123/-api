
from django.shortcuts import render,HttpResponse
from rest_framework import viewsets
# Create your views here.
from app.models import User,Test,Role
from app.serializers import UserSerializer,TestSerializer
from rest_framework import permissions

def create(request):
    """
    简单添加一下role
    :param request:
    :return:
    """
    Role.objects.create(role_name="学生")
    return HttpResponse("guanyu")

class UserViewSet(viewsets.ModelViewSet):
    """
    允许用户查看或编辑的API路径。
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class TestViewSet(viewsets.ModelViewSet):
    """
    允许用户查看或编辑的API路径。
    """
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Test.objects.all()
    serializer_class = TestSerializer
