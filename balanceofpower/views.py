from django.shortcuts import render, HttpResponse
from .forms import InfoForm
import pandas as pd

from django.contrib.staticfiles import finders
# Create your views here.
def index(request):
    #Basic - Doesnt need to be altered
    return render(request, 'index.html')

def formfill(request):
    form = InfoForm()
    return render(request, 'formfill.html',{'form':form})

def results(request):
    form = InfoForm(request.POST)
    if form.is_valid():
        pass  # Write code for processing the form information. The form information should be passed to appropriate functions for processing and finally call results function for display
    #Write information for displaying of results. All the required data is in the form.
    return render(request, 'results.html')

def input_output(selected_countries,selected_categories,weights):
	economy=pd.read_csv("data/economy.csv")
	society=pd.read_csv("data/society.csv")
	geography=pd.read_csv("data/geography.csv")
	demographics=pd.read_csv("data/demographics.csv")
	infrastructure=pd.read_csv("data/infrastructure.csv")
	dataframes=[economy,society,geography,demographics,infrastructure]
	truth_table=pd.concat(dataframes,axis=1,join='outer')
	



#Only for static files testing. No use in balance of power application
def test(request):
    result = finders.find('css/agency.css')
    if result==None:
        result = 'None'
    return HttpResponse(result)