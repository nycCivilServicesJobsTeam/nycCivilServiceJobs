# Generated by Django 3.1.2 on 2020-10-20 06:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signin', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_profile',
            name='user',
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.DeleteModel(
            name='User_Profile',
        ),
    ]
