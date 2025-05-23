# Generated by Django 4.1 on 2023-05-16 19:18

from django.db import migrations
import modelcluster.fields
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0025_release_live_release_release_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='latest_releases',
        ),
        migrations.AddField(
            model_name='homepage',
            name='body',
            field=wagtail.fields.StreamField([('latest_releases', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(default='Latest Releases', required=False)), ('limit', wagtail.blocks.IntegerBlock(default=3, label='Show maximum', required=True))]))], null=True, use_json_field=True),
        ),
        migrations.AlterField(
            model_name='release',
            name='artist_pages',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, related_name='releases', to='home.artistpage'),
        ),
    ]
