# Generated by Django 2.0.6 on 2018-06-28 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('databases', '0009_auto_20180628_1233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teams',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
