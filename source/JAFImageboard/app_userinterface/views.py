from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.generic import View, TemplateView, RedirectView, ListView
from django.utils import formats
from django.forms.models import model_to_dict

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
        _tpc = get_object_or_404(TopicModel, name=self.kwargs["tpc"])
        return ThreadModel.objects.filter(tpc=_tpc).order_by("-id")
    
    def get_context_data(self):
        context = super(ListView, self).get_context_data()
        context["tpc"] = self.kwargs["tpc"]
        context["title"] = "/" + self.kwargs["tpc"] + "/"
        context["form"] = NewThreadForm()
        return context


class NewThreadView(RedirectView):
    """Create new thread and redirect to it."""
    url = "/"
    def post(self, request, *args, **kwargs):
        form = NewThreadForm(request.POST)
        if form.is_valid():
            fresh_thread = ThreadModel(title=request.POST["thread_title"],
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
        _thr = get_object_or_404(ThreadModel, id=self.kwargs["thr"])
        return MessageModel.objects.filter(thr=_thr)

    def get_context_data(self):
        context = super(ListView, self).get_context_data()
        context["thr"] = self.kwargs["thr"]
        context["thr_title"] = ThreadModel.objects.get(id=self.kwargs["thr"]).title
        context["tpc"] = self.kwargs["tpc"]
        context["title"] = "/" + self.kwargs["tpc"] + "/"
        if context["messages"]:
            context["last_msg_id"] = context["messages"].reverse()[0]
        else:
            context["last_msg_id"] = 0
        context["form"] = MessageForm()
        return context

    def post(self, request, *args, **kwargs):
        if ("text" in request.POST):
            form = MessageForm(request.POST, request.FILES or None)
            if form.is_valid():
                fresh_message = form.save(commit=False)
                fresh_message.author_ip=request.META["REMOTE_ADDR"]
                fresh_message.tpc=TopicModel.objects.get(name=kwargs["tpc"])
                fresh_message.thr=ThreadModel.objects.get(id=kwargs["thr"])
                fresh_message.save()
        _thr = get_object_or_404(ThreadModel, id=self.kwargs["thr"])
        q = MessageModel.objects.filter(thr=_thr)
        q = q.filter(id__gt=request.POST["last_msg_id"])
        response = []
        d = {}
        for message in q:
            d["id"] = message.id
            d["text"] = message.text
            d["date"] = formats.date_format(message.date, format="DATETIME_FORMAT")
            d["url"] = '/static/' + message.pic_rel.name
            response.append(d)
        return JsonResponse(response, safe=False)


class RedirectToHomepage(RedirectView):
    """RedirectToHomepage"""
    url='/'