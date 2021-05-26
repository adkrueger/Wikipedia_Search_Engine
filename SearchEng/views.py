from SearchEng.forms import SearchForm
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.views import generic
from django.views.generic import FormView

from .models import SearchQuery, InfoResults
from .forms import SearchForm

# Create your views here. 
def index(request): 
    return HttpResponse("Hello, world!")

def manage_search(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(reverse('index'))
    else:
        form = SearchForm()
    
    return render(request, 'search_form.html', {'form': form})

class SearchFormView(FormView):
    form_class = SearchForm
    template_name = 'SearchEng/search_form.html'

    def get_success_url(self):
        return reverse('info')
    
    # def form_valid(self, form):

class IndexView(generic.ListView):
    template_name = 'SearchEng/index.html'
    model = SearchQuery

class PageInfoView(generic.ListView):
    template_name = 'SearchEng/page_info.html'
    model = InfoResults