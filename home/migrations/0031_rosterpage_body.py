# Generated by Django 4.1 on 2023-05-21 15:09

from django.db import migrations
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0030_artistpage_bio_alter_aboutpage_gaming_info_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='rosterpage',
            name='body',
            field=wagtail.fields.StreamField([('artists', wagtail.blocks.StructBlock([('artists', wagtail.blocks.ListBlock(wagtail.blocks.PageChooserBlock('home.ArtistPage', required=True), required=True))]))], null=True, use_json_field=True),
        ),
    ]
