from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def homepage(request):
    return HttpResponse("Hello, world. You're at the homepage.\
                    <br> It's supposed to be a list of available topics.\
                    <br> Check out thread <a href='/rus'>rus</a>, for example.\
                    <br> Or <a href='/vg'>vg</a>.\
                    <br> Actually, any combination of 2 or 3 letters will do.\
                    ")

def threadlist(request, tpc):
    return HttpResponse("This is list of threads for topic /" + tpc + "/.\
                        <br> You can choose from those:\
                        <br> <a href='/"+tpc+"/1'>1. First</a>\
                        <br> <a href='/"+tpc+"/2'>2. Second</a>\
                        <br> <a href='/"+tpc+"/3'>3. Third</a>" )

def threadpage(request, tpc, thr):
    return HttpResponse("This is thread page for thread №" + thr + " from topic /" + tpc + "/.")

def homepage_redirect(request):
    return HttpResponseRedirect("/")