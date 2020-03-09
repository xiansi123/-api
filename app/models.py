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
    body_points=models.IntegerField(choices=BODY_ITEM,default=3,verbose_name='身体素质')
    social_points=models.IntegerField(choices=SOCIAL_ITEM,default=3,verbose_name='社团情况')