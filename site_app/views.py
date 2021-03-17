from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView,DetailView,ListView,View,TemplateView
from site_app.models import ignisdata
from site_app.forms import AlldataForm
from django.shortcuts import redirect
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
import json


class EventListView (ListView):
    model= ignisdata
    context_object_name='events'
    template_name='EventList.html'

    def get_queryset(self):
        return ignisdata.objects.all()

class AddEvent(CreateView):
    model= ignisdata
    template_name='addEvents.html'
    form_class= AlldataForm

    def form_valid(self, form):
        
        event=form.save()
        print (event) 
        return redirect('EventList')

def toogleLike(request, pk):
    event = get_object_or_404(ignisdata, pk=pk)

    if request.method == "GET":
        if event.is_liked == True:
            event.is_liked = False
        else :
            event.is_liked = True

        event.save()
        return JsonResponse({'is_liked':event.is_liked})





