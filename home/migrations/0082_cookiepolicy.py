# Generated by Django 4.2.2 on 2023-11-10 14:49

from django.db import migrations, models
import django.db.models.deletion
import wagtailcache.cache


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0083_workflowcontenttype'),
        ('home', '0081_alter_playlist_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='CookiePolicy',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
            ],
            options={
                'abstract': False,
            },
            bases=(wagtailcache.cache.WagtailCacheMixin, 'wagtailcore.page'),
        ),
    ]
