from django.http import HttpResponse, HttpResponseServerError
from django.shortcuts import render
from django.views import generic

from . import models


# Create your views here.
def index(request):
    # print(request.META.REMOTE_USER)
    return HttpResponse("Hello Everyone")

def not_implemented(request):
    return HttpResponseServerError(f"{request.path} Not Implemented yet", 501)

class MainPage(generic.ListView):
    template_name = "home.html"
    context_object_name = "albumsubmissions"

    def get_queryset(self):
        return models.AlbumSubmission.objects.filter().order_by('-round')[:20]
