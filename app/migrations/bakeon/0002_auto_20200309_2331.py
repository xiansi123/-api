# Generated by Django 3.0.2 on 2020-03-09 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='work_points',
            field=models.IntegerField(choices=[(4, '优秀'), (3, '良好'), (2, '及格'), (1, '不及格')], default=3, verbose_name='作业数据'),
        ),
    ]
