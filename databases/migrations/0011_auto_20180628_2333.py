# Generated by Django 2.0.3 on 2018-06-28 15:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('databases', '0010_auto_20180628_1419'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teams',
            old_name='vertify',
            new_name='verify',
        ),
    ]