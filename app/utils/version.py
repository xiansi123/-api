from rest_framework.versioning import BaseVersioning,URLPathVersioning

# 这个return的version去哪了？
# 在drf的views文件(django系统的)中的APIView类的determine_version方法中调用
class ParamVersion(BaseVersioning):
     def determine_version(self, request, *args, **kwargs):
         # 获取原生的request中的['version']
         version=request.query_params.get('version')
         print(version)
         return version
class ParamVersion1(URLPathVersioning):
    pass