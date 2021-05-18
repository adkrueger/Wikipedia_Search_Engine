from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from .models import SearchQuery

# Create your views here. 
def index(request): 
    return HttpResponse("Hello, world!")

class IndexView(generic.ListView):
    template_name = 'SearchEng/index.html'
    model = SearchQuery
