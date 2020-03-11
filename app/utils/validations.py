from rest_framework import serializers
#自定义一个验证器
#
class MyValidator:
    # def __init__:
    #     pass
    def __call__(self,value):
        if not value.startswith('1'):
            message="必须以1开头"
            raise  serializers.ValidationError(message)