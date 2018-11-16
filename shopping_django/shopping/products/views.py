from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import product_details

def productView(request):

    return render(request,'products.html')

# Create your views here.
