
from rest_framework import serializers

from app.models import User,Test


class UserSerializer(serializers.HyperlinkedModelSerializer):
    # 这种方法也许也可以
    # tests = serializers.PrimaryKeyRelatedField(
    #                                     many=True,
    #                                     source='tests.all.values_list',
    #                                     queryset=Test.objects.all())

    # 自定义显示多对多关系中tests的名字
    tests =serializers.SerializerMethodField()
    def get_tests(self,row):
        tests_list = row.tests.all()
        ret=[]
        for item in tests_list:
            ret.append({'id':item.id,'test_name':item.test_name})
            # ret.append(item.test_name)
        return ret

    # get_work_points_display可执行callable，但不用加括号
    # source可以指定字段也可以指定可执行
    #使用post会报错，无论填写数字还是汉字 可能是没重写create方法？

    work_points=serializers.CharField(source='get_work_points_display')

    #唯一外键的添加方式
    role = serializers.CharField(source='role.role_name')

    class Meta:
        model = User
        fields = ('id','url','role', 'username','email', 'work_points','match_points','test_points','tests','match_points','body_points','social_points')

class TestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Test
        fields = ('test_name','users')

# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ('url', 'name')