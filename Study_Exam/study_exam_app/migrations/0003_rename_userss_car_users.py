# Generated by Django 3.2.3 on 2021-06-12 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('study_exam_app', '0002_car'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='userss',
            new_name='users',
        ),
    ]