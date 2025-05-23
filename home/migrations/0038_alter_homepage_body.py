# Generated by Django 4.1 on 2023-06-02 11:20

from django.db import migrations
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0037_artistpage_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.fields.StreamField([('latest_releases', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(default='Latest Releases', required=False)), ('limit', wagtail.blocks.IntegerBlock(default=3, label='Show maximum', required=True))])), ('artists', wagtail.blocks.StructBlock([('artists', wagtail.blocks.ListBlock(wagtail.blocks.PageChooserBlock('home.ArtistPage', required=True), required=True))])), ('latest_merch', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(default='Latest Merch', required=False)), ('limit', wagtail.blocks.IntegerBlock(default=3, label='Show maximum', required=True))]))], null=True, use_json_field=True),
        ),
    ]
