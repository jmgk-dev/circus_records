# Generated by Django 4.1 on 2023-05-13 13:54

from django.db import migrations
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_remove_merchpage_merchcat_merchpage_merch_catalogue'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutpage',
            name='gaming_info',
            field=wagtail.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='history',
            field=wagtail.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='mission_statement',
            field=wagtail.fields.RichTextField(blank=True),
        ),
    ]
