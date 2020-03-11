from django.views.generic.base import View
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import HttpResponse
from rest_framework import viewsets
# Create your views here.

from app.models import User,Test,Role
from app.utils.page import MyPagination
from app.utils.permission import MyPermission
from app.utils.serializers import UserSerializer, TestSerializer, RoleSerializer
from rest_framework import permissions

from app.utils.throttle import MyvisitThrottle3,MyvisitThrottle2
from app.utils.version import ParamVersion


def create(request):
    """
    简单添加一下role
    :param request:
    :return:
    """
    Role.objects.create(role_name="学生")

    return HttpResponse("OK")


# http://127.0.0.1:8000/api/users/点击过快会报错
class UserViewSet(viewsets.ModelViewSet):
    """
    允许用户查看或编辑的API路径。
    """
    #self.dispatch()
    pagination_class = MyPagination
    permission_classes = [MyPermission]
    versioning_class = ParamVersion
    throttle_classes = [MyvisitThrottle2,]
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class TestViewSet(viewsets.ModelViewSet):
    """
    允许用户查看或编辑的API路径。
    """
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Test.objects.all()
    serializer_class = TestSerializer

class PraseView(APIView):
    def post(self,request):
        print(request.data)
        return True


class RoleView(APIView):
    def post(self,request):
        print(request.data)
        role_ser=RoleSerializer(data=request.data)
        if role_ser.is_valid():
            print(role_ser.validated_data)
        else:
            print(role_ser.errors)
        # return HttpResponse('something')
        return Response('something')
