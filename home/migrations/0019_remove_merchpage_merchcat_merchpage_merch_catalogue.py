# Generated by Django 4.1 on 2023-05-08 18:01

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_remove_releasespage_releasecat_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='merchpage',
            name='merchcat',
        ),
        migrations.AddField(
            model_name='merchpage',
            name='merch_catalogue',
            field=wagtail.fields.StreamField([('merch_catalogue', wagtail.blocks.StructBlock([('merch', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('link', wagtail.blocks.URLBlock(required=True)), ('description', wagtail.blocks.CharBlock(required=True)), ('type', wagtail.blocks.CharBlock(required=True)), ('price', wagtail.blocks.CharBlock(required=True))])))]))], null=True, use_json_field=True),
        ),
    ]
