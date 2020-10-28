from django.urls import include, path
from django.views.generic.base import TemplateView

from . import views

urlpatterns = [
    # home page
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    # master list for listening group
    # album page view
    # album submission page - create Album and AlbumSubmission
    # users album review view
    # users album review form
    # view themes
]
