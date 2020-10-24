from django.http import HttpResponse, HttpResponseServerError
from django.shortcuts import render


# Create your views here.
def index(request):
    # print(request.META.REMOTE_USER)
    return HttpResponse("Hello Everyone")

def not_implemented(request):
    return HttpResponseServerError(f"{request.path} Not Implemented yet", 501)
