# Generated by Django 3.1.6 on 2021-05-02 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tunr', '0007_auto_20210207_1031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='photo_url',
            field=models.TextField(verbose_name='your photo'),
        ),
    ]
