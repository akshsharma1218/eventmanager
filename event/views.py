from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from django.db.models import Q

def home(request):
    event = Event.objects.all()
    context={"Event":event}
    return render (request,"event/home.html",context)

def liked_event(request):
    event = Event.objects.filter(is_liked=True)
    context={"Event":event}
    return render (request,"event/liked_event.html",context)

def like_event(request):
    event = get_object_or_404(Event,id=request.POST.get('id'))
    print(event, event.is_liked)
    if event.is_liked:
        event.is_liked=False
    else:
        event.is_liked=True
    event.save()
    context={
            'event':event,
    }
    if request.is_ajax():
        html = render_to_string('event/like_section.html', context, request = request)
        return JsonResponse({ 'form': html })


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'event/register.html', {'form': form})

class EventCreateView(LoginRequiredMixin,CreateView):
    model   = Event
    fields  = ["event_name","data","time","location","image"]

class SearchResultView(ListView):
    model = Event
    template_name='event/search_result.html'

    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = Event.objects.filter(Q(event_name__icontains=query))
        print(object_list)
        return object_list
