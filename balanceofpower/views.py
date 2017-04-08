from django.shortcuts import render, HttpResponse
from .forms import InfoForm

from django.contrib.staticfiles import finders
# Create your views here.
def index(request):
    #Basic - Doesnt need to be altered
    return render(request, 'index.html')

def formfill(request):
    form = InfoForm()
    return render(request, 'formfill.html',{'form':form})

def latest(request):
    #Basic - Doesnt need to be altered
    return render(request, 'latest.html')

def results(request):
    form = InfoForm(request.POST)
    if form.is_valid():
        pass  # Write code for processing the form information. The form information should be passed to appropriate functions for processing and finally call results function for display
    #Write information for displaying of results. All the required data is in the form.
    return render(request, 'results.html')


#Only for static files testing. No use in balance of power application
def test(request):
    result = finders.find('css/agency.css')
    if result==None:
        result = 'None'
    return HttpResponse(result)