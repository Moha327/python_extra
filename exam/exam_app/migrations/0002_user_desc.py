# Generated by Django 2.2.4 on 2021-05-31 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='desc',
            field=models.TextField(default=2),
            preserve_default=False,
        ),
    ]