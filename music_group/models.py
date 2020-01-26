from django.db import models
from django.contrib.auth.models import User

_album_types = ['single', 'EP', 'studio', 'double EP', 'live']


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


class AlbumSubmission(models.Model):
    """an album submitted to a listening group"""
    # TODO: make album/submittedOn nullable to queue up picks
    album = models.ForeignKey(Album, on_delete=models.PROTECT)
    submittedOn = models.DateTimeField(auto_now=True)
    submittedBy = models.ForeignKey(User, on_delete=models.PROTECT)
    submittedTo = models.ForeignKey(ListeningGroup, on_delete=models.PROTECT)
    # TODO: normalize?
    theme = models.CharField(max_length=100)


class AlbumReview(models.Model):
    """comments from a user on an album"""
    reviewedBy = models.ForeignKey(User, on_delete=models.PROTECT)
    reviewedOn = models.DateTimeField(auto_now=True)
    comment = models.TextField()
    favouriteTrack = models.CharField(max_length=100)

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
