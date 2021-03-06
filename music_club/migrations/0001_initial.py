# Generated by Django 3.0.2 on 2020-01-25 23:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('length', models.DurationField()),
                ('tracks', models.IntegerField()),
                ('albumType', models.CharField(choices=[('0', 'single'), ('1', 'EP'), ('2', 'studio'), ('3', 'double EP'), ('4', 'live')], default='0', max_length=15)),
                ('artist', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=40)),
                ('genre', models.CharField(max_length=40)),
                ('label', models.CharField(max_length=40)),
                ('subgenre', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='ListeningGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('users', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AlbumSubmission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submittedOn', models.DateTimeField(auto_now=True)),
                ('theme', models.CharField(max_length=100)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='music_club.Album')),
                ('submittedBy', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('submittedTo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='music_club.ListeningGroup')),
            ],
        ),
        migrations.CreateModel(
            name='AlbumReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reviewedOn', models.DateTimeField(auto_now=True)),
                ('comment', models.TextField()),
                ('favouriteTrack', models.CharField(max_length=100)),
                ('reviewedBy', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
