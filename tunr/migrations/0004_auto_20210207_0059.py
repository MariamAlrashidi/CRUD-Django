# Generated by Django 3.1.5 on 2021-02-06 21:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tunr', '0003_auto_20210207_0058'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='color',
        ),
        migrations.RemoveField(
            model_name='song',
            name='color_2',
        ),
    ]
