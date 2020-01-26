# Generated by Django 3.0.2 on 2020-01-26 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_group', '0003_auto_20200126_0402'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='albumreview',
            name='comment',
        ),
        migrations.AddField(
            model_name='albumreview',
            name='review',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='theme',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
