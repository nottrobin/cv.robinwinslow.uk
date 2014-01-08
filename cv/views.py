from django.shortcuts import render
from urllib import urlopen
from django.http import HttpResponse
from django.core import urlresolvers
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView
from io import BytesIO
import json
import gzip
from cv.profiles import repositories, reputation

class CvTemplateView(TemplateView):
    def get_context_data(self):
        name_classes = {}

        for name in url_names():
            path = reverse(name)
            name_classes[name] = 'current' if self.request.get_full_path() == path else ''

        return { 'name_classes': name_classes }

def profiles(request):
    profiles = {
        'repositories' : repositories(),
        'reputation' : reputation()
    }

    return HttpResponse(
        content = json.dumps(profiles),
        mimetype = 'application/json'
    )

def url_names():
    resolvers = urlresolvers.get_resolver(None).reverse_dict.items()
    named_resolvers = filter(lambda x: type(x[0]) is str, resolvers)
    url_names = [x[0] for x in named_resolvers]

    return url_names
