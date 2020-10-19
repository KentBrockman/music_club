import datetime

from django.contrib.auth.models import User
from django.db import models

_album_types = ['single', 'EP', 'studio', 'double EP', 'live']
_expectations = ['Well Below', 'Below', 'Slightly Below',
                 'Met', 'Slightly Above', 'Above', 'Well Above']


class Album(models.Model):
    """collection of music"""
    ALBUM_TYPE_CHOICES = [(str(i), _album_types[i])
                          for i in range(len(_album_types))]
    title = models.CharField(max_length=100)
    year = models.IntegerField()
    length = models.DurationField()
    tracks = models.IntegerField()
    albumType = models.CharField(
        max_length=15, choices=ALBUM_TYPE_CHOICES, default='0')

    # TODO: normalize?
    artist = models.CharField(max_length=100)
    country = models.CharField(max_length=40)
    genre = models.CharField(max_length=40)
    label = models.CharField(max_length=40)
    subgenre = models.CharField(max_length=40)

    # TODO: album covers?


class ListeningGroup(models.Model):
    """a group of user that listen to music together and share reviews"""
    name = models.CharField(max_length=200)
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.name


class Theme(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(default='')


class AlbumSubmission(models.Model):
    """an album submitted to a listening group"""
    # TODO: make album/submittedOn nullable to queue up picks
    album = models.ForeignKey(Album, on_delete=models.PROTECT)
    submittedOn = models.DateTimeField(auto_now=True)
    submittedBy = models.ForeignKey(User, on_delete=models.PROTECT)
    submittedTo = models.ForeignKey(ListeningGroup, on_delete=models.PROTECT)
    round = models.IntegerField(default=0)
    theme = models.ForeignKey(
        Theme, on_delete=models.PROTECT, blank=True, null=True)


class AlbumReview(models.Model):
    """comments from a user on an album"""
    EXPECTATIONS_CHOICES = [(str(i), _expectations[i])
                            for i in range(len(_expectations))]
    album = models.ForeignKey(Album, on_delete=models.PROTECT)
    reviewedBy = models.ForeignKey(User, on_delete=models.PROTECT)
    reviewedOn = models.DateField(default=datetime.date.today)
    review = models.TextField(null=True, blank=True)
    favouriteTrack = models.CharField(max_length=100)
    expectations = models.CharField(
        max_length=16, choices=EXPECTATIONS_CHOICES, default='3')


# TODO: ranking approaches
# connect to album review
# have different kinds of rankings. add more later
# class OrderedRanking(models.Model):
#     """rank all reviewed albums in order of preference"""
#     review = models.ForeignKey(AlbumReview, on_delete=models.CASCADE)
#     place = models.IntegerField()

# class StarRanking(models.Model):
#     review = models.ForeignKey(AlbumReview, on_delete=models.CASCADE)
#     stars = models.DecimalField()

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    comment = models.TextField()
    submittedOn = models.DateTimeField(auto_now=True)

    # comments can be on one of the following:
    # TODO: validation rule for this?
    # TODO: verify ManyToOne nature of relationship here
    on_album = models.ForeignKey(
        Album, on_delete=models.CASCADE, null=True, blank=True, related_name='comments')
    on_submission = models.ForeignKey(
        AlbumSubmission, on_delete=models.CASCADE, null=True, blank=True, related_name='comments')
    on_review = models.ForeignKey(
        AlbumReview, on_delete=models.CASCADE, null=True, blank=True, related_name='comments')
    on_theme = models.ForeignKey(
        Theme, on_delete=models.CASCADE, null=True, blank=True, related_name='comments')
