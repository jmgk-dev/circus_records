# Generated by Django 4.1 on 2023-06-22 11:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0067_alter_artistpage_body'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artistpage',
            name='body',
        ),
    ]
