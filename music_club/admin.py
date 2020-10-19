from django.contrib import admin

from .models import Album, ListeningGroup, AlbumSubmission, Theme

# let managers override albums
admin.site.register(Album)
# let managers set up listening groups
admin.site.register(ListeningGroup)
# let managers set up album submissions
admin.site.register(AlbumSubmission)
# let managers set up themes
admin.site.register(Theme)
