from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template("index.jinja")
    return HttpResponse(template.render())


def api_docs(request):
    template = loader.get_template("api_docs.jinja")
    return HttpResponse(template.render())
