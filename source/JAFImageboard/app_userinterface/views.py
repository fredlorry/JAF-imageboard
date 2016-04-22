from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.generic import View, TemplateView, RedirectView, ListView
from django.utils import formats

from .models import MessageModel, TopicModel, ThreadModel
from .forms import MessageForm, NewThreadForm
# Create your views here.


class HomepageView(ListView):
    """Homepage view."""
    template_name = "homepage.html"
    context_object_name = "topics"
    def get_queryset(self):
        return TopicModel.objects.order_by('name')
    def get_context_data(self):
        context = super(ListView, self).get_context_data()
        context['title'] = "Homepage"
        return context


class ThreadlistView(ListView):
    """Threadlist view."""
    template_name = "threadlist.html"
    context_object_name = "threads"

    def get_queryset(self):
        self.tpc = get_object_or_404(TopicModel, name=self.kwargs["tpc"])
        return ThreadModel.objects.filter(tpc=self.tpc).order_by("-id")
    
    def get_context_data(self):
        context = super(ListView, self).get_context_data()
        context["tpc"] = self.kwargs["tpc"]
        context["title"] = "/" + self.kwargs["tpc"] + "/"
        context["form"] = NewThreadForm()
        return context


class NewThreadView(RedirectView):
    """Create new thread and redirect to it."""
    url="/"
    def post(self, request, *args, **kwargs):
        form = NewThreadForm(request.POST)
        if form.is_valid():
            fresh_thread = ThreadModel(title=request.POST["title"],
                                        tpc=TopicModel.objects.get(name=kwargs["tpc"])
                                        )
            fresh_thread.save()
            return HttpResponseRedirect("/" + self.kwargs["tpc"] + "/" + str(fresh_thread.id) + "/")
        else:
            return HttpResponseRedirect("/" + self.kwargs["tpc"] + "/")
            
    def get(self, request, *args, **kwargs):
        url = "/" + kwargs["tpc"] + "/"
        return super(RedirectView, self).get(self, request, *args, **kwargs)


class ThreadpageView(ListView):
    """Threadpage view."""
    
    template_name = "threadpage.html"
    context_object_name = "messages"

    def get_queryset(self):
        self.thr = get_object_or_404(ThreadModel, id=self.kwargs["thr"])
        return MessageModel.objects.filter(thr=self.thr)

    def get_context_data(self):
        context = super(ListView, self).get_context_data()
        context["thr"] = self.kwargs["thr"]
        context["thr_title"] = ThreadModel.objects.get(id=self.kwargs["thr"]).title
        context["tpc"] = self.kwargs["tpc"]
        context["title"] = "/" + self.kwargs["tpc"] + "/"
        context["form"] = MessageForm()
        return context

    def post(self, request, *args, **kwargs):
        form = MessageForm(request.POST)
        if form.is_valid():
            fresh_message = MessageModel(text=form.cleaned_data["message_text"],
                                        author_ip=request.META["REMOTE_ADDR"],
                                        tpc=TopicModel.objects.get(name=kwargs["tpc"]),
                                        thr=ThreadModel.objects.get(id=kwargs["thr"])
                                        )
            fresh_message.save()
        model = MessageModel.objects.filter(thr=kwargs["thr"]).latest("pk")
        response = {}
        response["messageId"] = model.id
        response["messageText"] = model.text
        response["messageDate"] = formats.date_format(model.date, "DATETIME_FORMAT")
        return JsonResponse(response)


class RedirectToHomepage(RedirectView):
    """RedirectToHomepage"""
    url='/'