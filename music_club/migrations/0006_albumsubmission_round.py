# Generated by Django 3.0.7 on 2020-10-19 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_club', '0005_auto_20200126_0420'),
    ]

    operations = [
        migrations.AddField(
            model_name='albumsubmission',
            name='round',
            field=models.IntegerField(default=0),
        ),
    ]