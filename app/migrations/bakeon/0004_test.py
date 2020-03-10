# Generated by Django 3.0.2 on 2020-03-09 19:53

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20200309_2332'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_name', models.CharField(max_length=128, verbose_name='考试名')),
                ('users', models.ManyToManyField(related_name='tests', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
