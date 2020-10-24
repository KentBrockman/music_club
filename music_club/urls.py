from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # login page
    # home page for user
    # master list for listening group
    # album page view
    # album submission page - create Album and AlbumSubmission
    # users album review view
    # users album review form
    # view themes
]
