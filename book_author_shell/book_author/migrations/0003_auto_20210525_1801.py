# Generated by Django 2.2.4 on 2021-05-25 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_author', '0002_auto_20210524_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='desc',
            field=models.TextField(default='programming book'),
            preserve_default=False,
        ),
    ]
