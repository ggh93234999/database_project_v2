# Generated by Django 2.0.6 on 2018-06-27 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('databases', '0005_auto_20180626_1612'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_profiles',
            name='is_confirmation',
        ),
        migrations.RemoveField(
            model_name='user_profiles',
            name='token',
        ),
    ]
