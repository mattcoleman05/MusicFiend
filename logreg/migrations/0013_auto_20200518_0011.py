# Generated by Django 2.2 on 2020-05-18 00:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logreg', '0012_auto_20200517_2351'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='user',
            name='updated_at',
        ),
    ]