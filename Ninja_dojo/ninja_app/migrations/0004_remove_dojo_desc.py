# Generated by Django 2.2.4 on 2021-05-24 16:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ninja_app', '0003_auto_20210523_1831'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dojo',
            name='desc',
        ),
    ]
