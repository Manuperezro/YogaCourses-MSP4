# Generated by Django 3.2.13 on 2022-07-03 19:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0006_rename_video_url_video_dideourl'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='dideoUrl',
            new_name='video_url',
        ),
    ]
