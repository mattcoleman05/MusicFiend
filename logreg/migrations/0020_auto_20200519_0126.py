# Generated by Django 3.0.5 on 2020-05-19 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logreg', '0019_artistimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artistinfo',
            name='profile',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='artistinfo',
            name='record_label',
            field=models.CharField(max_length=50),
        ),
    ]
