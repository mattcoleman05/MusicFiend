# Generated by Django 2.2 on 2020-05-18 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logreg', '0018_auto_20200518_0345'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArtistImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('artist_image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
