# Generated by Django 2.2 on 2020-05-17 05:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logreg', '0003_auto_20200517_0413'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Artist',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
