# Generated by Django 2.2.6 on 2019-11-04 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aiqu', '0002_test_pingtai'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test',
            name='pingtai',
        ),
    ]