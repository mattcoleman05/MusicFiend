# Generated by Django 2.2 on 2020-05-17 07:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logreg', '0008_albuminfo_artistinfo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artistinfo',
            name='user',
        ),
        migrations.DeleteModel(
            name='AlbumInfo',
        ),
        migrations.DeleteModel(
            name='ArtistInfo',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
