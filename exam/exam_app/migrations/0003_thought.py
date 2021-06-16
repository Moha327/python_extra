# Generated by Django 2.2.4 on 2021-05-31 09:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exam_app', '0002_user_desc'),
    ]

    operations = [
        migrations.CreateModel(
            name='Thought',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.TextField()),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('likedBy', models.ManyToManyField(related_name='likes', to='exam_app.User')),
                ('uploadeBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='createdThoughts', to='exam_app.User')),
            ],
        ),
    ]
