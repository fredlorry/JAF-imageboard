from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View, TemplateView

# Create your views here.

class HomepageView(TemplateView):
    """Homepage view."""
    template_name = "homepage.html"


class ThreadlistView(TemplateView):
    """Threadlist view."""
    template_name = "threadlist.html"

class ThreadpageView(TemplateView):
    """Threadpage view."""
    template_name = "threadpage.html"

def homepage_redirect(request):
    return HttpResponseRedirect("/")