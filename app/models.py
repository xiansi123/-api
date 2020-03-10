from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser,models.Model):
    WORK_ITEM =[
        (4,'优秀'),
        (3,'良好'),
        (2, '及格'),
        (1, '不及格'),
    ]
    BODY_ITEM =[
        (4,'过硬'),
        (3,'健康'),
        (2, '亚健康'),
        (1, '生病'),
    ]
    SOCIAL_ITEM =[
        (4,'积极'),
        (3,'一般'),
        (2, '很少'),
        (1, '排斥'),
    ]
    work_points=models.IntegerField(choices=WORK_ITEM,default=3,verbose_name='作业数据')
    match_points=models.FloatField(verbose_name='比赛成绩',default=0.0)
    test_points=models.FloatField(verbose_name='考试成绩',default=0.0)
    #
    role=models.ForeignKey('Role',on_delete=models.CASCADE,default=1)
    body_points=models.IntegerField(choices=BODY_ITEM,default=3,verbose_name='身体素质')
    social_points=models.IntegerField(choices=SOCIAL_ITEM,default=3,verbose_name='社团情况')

# 后期添加这个Role
# 报错You are trying to add a non-nullable field 'role'
# to user without a default; we can't do that
# (the database needs something to populate existing rows)
# 解决 删库重建 不是长久之道
class Role(models.Model):
    # id=models.AutoField(primary_key=True)
    role_name=models.CharField(max_length=128,verbose_name="角色名",default='学生')

class Test(models.Model):
    test_name=models.CharField(max_length=128,verbose_name="考试名")
    users = models.ManyToManyField('User',related_name='tests',)
