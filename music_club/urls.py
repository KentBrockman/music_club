from django.urls import include, path
from django.views.generic.base import TemplateView

from . import views

urlpatterns = [
    # home page
    path('', views.MainPage.as_view(), name='home'),
    # master list for listening group
    # album page view
    # album submission page - create Album and AlbumSubmission
    # users album review form

    # themes
    # view
    # vote
    # submit/manage
]
