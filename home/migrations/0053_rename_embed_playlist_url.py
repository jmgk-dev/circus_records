# Generated by Django 4.1 on 2023-06-04 19:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0052_playlist_headline'),
    ]

    operations = [
        migrations.RenameField(
            model_name='playlist',
            old_name='embed',
            new_name='url',
        ),
    ]
