from django.shortcuts import render
from urllib import urlopen
from django.http import HttpResponse
from django.views.generic import TemplateView
from io import BytesIO
import json
import gzip
from cv.profiles import repositories, reputation

class HomeView(TemplateView):
    template_name="cv/index.html"

def profiles(request):
    profiles = {
        'repositories' : repositories(),
        'reputation' : reputation()
    }

    return HttpResponse(
        content = json.dumps(profiles),
        mimetype = 'application/json'
    )
