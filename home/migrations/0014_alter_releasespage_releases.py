# Generated by Django 4.1 on 2023-05-03 18:40

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_alter_releasespage_releases'),
    ]

    operations = [
        migrations.AlterField(
            model_name='releasespage',
            name='releases',
            field=wagtail.fields.StreamField([('releases', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('link', wagtail.blocks.URLBlock(required=True)), ('artist', wagtail.blocks.CharBlock(required=True)), ('title', wagtail.blocks.CharBlock(required=True))]))], null=True, use_json_field=True),
        ),
    ]
