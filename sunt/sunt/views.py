from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader
from django.shortcuts import render

def index(request): # vista
  return render(request, "index.html")

def sobrenosotros(request):
  return render(request, "sobrenosotros.html") 

def normas(request):
  return render(request, "normas.html")  

def tramites(request):
  return render(request, "tramites.html")    

