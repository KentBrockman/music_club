# Generated by Django 3.0.7 on 2020-10-19 17:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music_club', '0006_albumsubmission_round'),
    ]

    operations = [
        migrations.AddField(
            model_name='albumreview',
            name='album',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='music_club.Album'),
            preserve_default=False,
        ),
    ]