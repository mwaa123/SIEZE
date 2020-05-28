from django.shortcuts import render,redirect
from django.http  import HttpResponse
from django.http  import HttpResponse,Http404
# Create your views here.

def welcome(request):
    
    return render(request,'fold/welcome.html')

def about(request):
    
    return render(request,'fold/about.html')

def pic(request):
    
    return render(request,'fold/pic.html')
