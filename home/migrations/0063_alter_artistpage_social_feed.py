# Generated by Django 4.1 on 2023-06-18 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0062_alter_artistpage_social_feed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artistpage',
            name='social_feed',
            field=models.CharField(blank=True, max_length=800, null=True),
        ),
    ]
