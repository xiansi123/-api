
from rest_framework import serializers

from app.models import User,Test
from app.utils.validations import MyValidator


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"#('tests',)
        # depth=1
    def validate_username(self,value):
        print(value)
        return value
    def validate_data(self):
        print(self)
        return self

# class UserSerializer(serializers.ModelSerializer):
#     # 这种方法也许也可以
#     #  关注每个field的to_representation方法和lookup_field字段
#     # tests = serializers.PrimaryKeyRelatedField(
#     #                                     many=True,
#     #                                     source='tests.all.values_list',
#     #                                     queryset=Test.objects.all())
#
#     # 自定义显示多对多关系中tests的名字
#     tests =serializers.SerializerMethodField()
#     def get_tests(self,row):
#         tests_list = row.tests.all()
#         ret=[]
#         for item in tests_list:
#             ret.append({'id':item.id,'test_name':item.test_name})
#             # ret.append(item.test_name)
#         return ret
#
#     # get_work_points_display可执行callable，但不用加括号
#     # source可以指定字段也可以指定可执行
#     #使用post会报错，无论填写数字还是汉字，可能是没重写create方法？
#     work_points=serializers.CharField(source='get_work_points_display')
#
#     # 唯一外键的添加方式
#     role = serializers.CharField(source='role.role_name')
#     class Meta:
#         model = User
#         fields = ('id','url','role', 'username','email', 'work_points','match_points','test_points','tests','match_points','body_points','social_points')

class TestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Test
        fields = ('test_name','users')

class RoleSerializer(serializers.Serializer):

    # 这里还没指定model所以字段可以任意
    # 自定义验证方法 1
    num = serializers.CharField(validators=[MyValidator()])

    # 自定义验证方法 2
    name = serializers.CharField()
    # 钩子函数
    def validate_name(self,value):
        print("自定义validate中的",value)
        return value