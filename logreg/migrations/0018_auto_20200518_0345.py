# Generated by Django 2.2 on 2020-05-18 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logreg', '0017_artistinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artistinfo',
            name='link',
            field=models.URLField(max_length=100),
        ),
        migrations.AlterField(
            model_name='artistinfo',
            name='record_label',
            field=models.URLField(max_length=50),
        ),
    ]
